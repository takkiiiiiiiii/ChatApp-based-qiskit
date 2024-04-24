# ==================================================================================== #
# qkd/bb84.py

from sys import argv, exit
from qiskit import *
from qiskit import QuantumCircuit, Aer, execute
from random import seed, sample
from IPython.display import display
import json


backend = Aer.get_backend('qasm_simulator')


def bb84(user0, user1, num_qubits, len_key):
    alice_bits = qrng(num_qubits)
    alice_basis = qrng(num_qubits)
    bob_basis = qrng(num_qubits)
    eve_basis = qrng(num_qubits)

    # Alice generates qubits 
    qc = compose_quantum_circuit(num_qubits, alice_bits, alice_basis)

    # Eve eavesdrops Alice's qubits
    qc, eve_bits = intercept_resend(qc, eve_basis)

    # Comparison their basis between Alice and Eve
    ae_basis, ae_match = check_bases(alice_basis, eve_basis)
    # Comparison their bits between Alice and Eve
    # ae_bits = check_bits(alice_bits,eve_bits,ae_basis)

    # Bob measure Alice's qubit
    qc, bob_bits = bob_measurement(qc,bob_basis)

    # eb_basis, eb_matches = check_bases(eve_basis,bob_basis)
    # eb_bits = check_bits(eve_bits,bob_bits,eb_basis)

    altered_qubits = 0

    user0.create_socket_for_classical()
    user1.create_socket_for_classical()
    sender_classical_channel = user0.socket_classical
    receiver_classical_channel = user1.socket_classical

    # Alice sifted key
    ka=''
    # Bob sifted key
    kb=''
    # Eve sifted key
    ke=''

    # アリスとボブ間で基底は一致のはずだが、ビット値が異なる(ノイズや盗聴者によるエラー)数
    err_num = 0

    # Announce bob's basis
    receiver_classical_channel.send(bob_basis.encode('utf-8'))
    bob_basis = sender_classical_channel.recv(4096).decode('utf-8')
    # Alice's side
    ab_basis, ab_matches = check_bases(alice_basis,bob_basis)
    ab_bits = check_bits(alice_bits, bob_bits, ab_basis)

    for i in range(num_qubits):
        if ae_basis[i] != 'Y' and ab_basis[i] == 'Y': # アリスとイヴ間で基底は異なる(量子ビットの状態が変わる)、アリスとボブ間では一致
            altered_qubits += 1
        if ab_basis[i] == 'Y': # アリスとボブ間で基底が一致
            ka += alice_bits[i] 
            kb += bob_bits[i]
        if ae_basis[i] == 'Y': # アリスとイヴ間で基底が一致
            ke += eve_bits[i]
        if ab_bits[i] == '!': # アリスとボブ間で基底は一致のはずだが、ビット値が異なる (イヴによって、量子ビットの状態が変化)
            err_num += 1
    err_str = ''.join(['!' if ka[i] != kb[i] else ' ' for i in range(len(ka))])

    print("Alice's remaining bits: " + ka)
    print("Error positions:        " + err_str)
    print("Bob's remaining bits:   " + kb)

# Final key agreement process

    selection_size = int(ab_matches/3)
    seed(64)
    selection_sender = [list(pair) for pair in sample(list(enumerate(ka)), selection_size)]

    # Alice sends the key information of random position
    json_data = json.dumps(selection_sender)
    byte_data = json_data.encode('utf-8')
    sender_classical_channel.send(byte_data)

    # Bob get the key information 
    received_key_info = receiver_classical_channel.recv(4096)
    received_string = received_key_info.decode('utf-8')
    original_key_info = json.loads(received_string)


    error_found = 0
    # Bob compare the positions of his own key with information based on indices
    print(original_key_info)
    for pair in original_key_info:
        if kb[pair[0]] != pair[1]:
            error_found += 1
            print("Bob realize that Eve interfered and abort the protocol. Then Bob sends Alice that.")
            receiver_classical_channel.send('False'.encode('utf-8'))

    sender_classical_channel.close()
    receiver_classical_channel.close()

    if error_found > 0:
        return -1, -1
    else:      
        # Compare each basis
        sender_key, receiver_key = compare_bases(num_qubits, ab_basis, ab_bits, alice_bits, bob_bits)
        
        return sender_key, receiver_key


def qrng(n):
    # generate n-bit string from measurement on n qubits using QuantumCircuit
    qc = QuantumCircuit(n,n)
    for i in range(n):
        qc.h(i) # The Hadamard gate has the effect of projecting a qubit to a 0 or 1 state with equal probability.
    # measure qubits 0, 1 & 2 to classical bits 0, 1 & 2 respectively
    qc.measure(list(range(n)),list(range(n)))
    # shot - Number of repetitions of each circuit for sampling
    # Return the results of the job.
    result = execute(qc,backend,shots=1).result() 
    bits = list(result.get_counts().keys())[0] 
    bits = ''.join(list(reversed(bits)))
    return bits


# qubit encodings in specified bases
def encode_qubits(n,k,a):
    # Create quantum circuit with n qubits and n classical bits
    qc = QuantumCircuit(n,n) 
    for i in range(n):
        if a[i] == '0':
            if k[i] == '1':
                qc.x(i)
        else:
            if k[i] == '0':
                qc.h(i)
            else: 
                qc.x(i)
                qc.h(i) 
    qc.barrier()
    return qc


# qubit measurements in specified bases
# b = Bob's basis infomation
def bob_measurement(qc,b):
    l = len(b)
    for i in range(l): 
        if b[i] == '1': # In case of Diagonal basis
            qc.h(i)

    qc.measure(list(range(l)),list(range(l))) 
    result = execute(qc,backend,shots=1).result() 
    bits = list(result.get_counts().keys())[0]
    bits = ''.join(list(reversed(bits)))

    qc.barrier() 
    return [qc,bits]


# check where bases matched
def check_bases(b1,b2):
    check = ''
    matches = 0
    for i in range(len(b1)):
        if b1[i] == b2[i]: 
            check += "Y" 
            matches += 1
        else:
            check += "-"
    return [check,matches]


# check where measurement bits matched
def check_bits(b1,b2,bck):
    check = ''
    for i in range(len(b1)):
        if b1[i] == b2[i] and bck[i] == 'Y':
            check += 'Y'
        elif b1[i] == b2[i] and bck[i] != 'Y':
            check += 'R'
        elif b1[i] != b2[i] and bck[i] == 'Y':
            check += '!'
        elif b1[i] != b2[i] and bck[i] != 'Y':
            check += '-'

    return check


def compose_quantum_circuit(n, alice_bits, a) -> QuantumCircuit:
    qc = QuantumCircuit(n,n)
    qc.measure_all()
    qc.compose(encode_qubits(n, alice_bits, a), inplace=True)
    return qc

def compare_bases(n, ab_bases, ab_bits, alice_bits, bob_bits):
    ka = ''  # kaの初期化
    kb = ''  # kbの初期化
    for i in range(n):
        if ab_bases[i] == 'Y':
            ka += alice_bits[i]
            kb += bob_bits[i]
    return ka, kb

# capture qubits, measure and send to Bob
def intercept_resend(qc,e):
    backend = Aer.get_backend('qasm_simulator') 
    l = len(e)

    for i in range(l):
        if e[i] == '1':
            qc.h(i)

    display(qc.draw())
    qc.measure(list(range(l)),list(range(l))) 
    result = execute(qc,backend,shots=1).result() 
    bits = list(result.get_counts().keys())[0] 
    bits = ''.join(list(reversed(bits)))

    qc.reset(list(range(l))) # Reset the quantum bit(s) to their default state すべての量子ビットの状態を|0>にする
    

    # イヴの情報を元に、アリスと同じエンコードをして、量子ビットの偏光状態を決める
    for i in range(l):
        if e[i] == '0':
            if bits[i] == '1':
                qc.x(i)
        else:
            if bits[i] == '0':
                qc.h(i)
            else:
                qc.x(i)
                qc.h(i)
    # Qiskit回路における「バリア（barrier）」は、量子ビットの状態に影響を与えない特別な操作で、回路設計や最適化において視覚的・操作的な支援を提供　
    qc.barrier()
    display(qc.draw())
    return [qc,bits]

# check where bases matched
# def check_bases(b1,b2):
#     check = ''
#     matches = 0
#     for i in range(len(b1)):
#         if b1[i] == b2[i]: 
#             check += "Y" 
#             matches += 1
#         else:
#             check += "-"
#     return [check,matches]

# # check where measurement bits matched
# def check_bits(b1,b2,bck):
#     check = ''
#     for i in range(len(b1)):
#         if b1[i] == b2[i] and bck[i] == 'Y':
#             check += 'Y'
#         elif b1[i] == b2[i] and bck[i] != 'Y':
#             check += 'R'
#         elif b1[i] != b2[i] and bck[i] == 'Y':
#             check += '!'
#         elif b1[i] != b2[i] and bck[i] != 'Y':
#             check += '-'

#     return check



# def channel(qc: QuantumCircuit) -> QuantumCircuit:
#     # error rate
#     error_kraus = kraus_error([[[1, 0], [0, (1 - error_prob)**0.5]],
#                           [[0, error_prob**0.5], [0, 0]]])
#     # クラウス演算子を使用してノイズモデルを構築
#     # 量子チャネルでのノイズによる量子情報の変化を再現
#     # Reproducing changes in quantum information due to noise in the quantum channel.
#     noise_model = NoiseModel()
#     noise_model.add_quantum_error(error_kraus, 'x', list(len(n)))
    
#     transpiled_qc = transpile(qc, basis_gates=backend.configuration().basis_gates)
#     backend.run(transpiled_qc)

#     return qc
