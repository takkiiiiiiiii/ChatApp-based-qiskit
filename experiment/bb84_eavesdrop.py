from qiskit import QuantumCircuit, Aer, execute
from qiskit_aer.noise import (NoiseModel, QuantumError, pauli_error, depolarizing_error)
from kr_Hamming import key_reconciliation_Hamming
from IPython.display import display
from qiskit.tools.visualization import plot_histogram
import numpy as np
import time
import random




count = 100
sifted_key_length = 1001
num_qubits_linux = 10 # for Linux
num_qubits_mac = 24 # for mac
backend = Aer.get_backend('qasm_simulator')


class User:
    def __init__(self, username: str, sharekey, socket_classical, socket_quantum):
        self.username = username
        self.sharekey = sharekey
        self.socket_classical = socket_classical
        self.socket_quantum = socket_quantum

    def create_socket_for_classical(self):
        import socket
        SERVER_HOST_CLASSICAL = '127.0.0.1'
        SERVER_PORT_CLASSICAL = 12001
        client_socket_classical = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket_classical.connect((SERVER_HOST_CLASSICAL, SERVER_PORT_CLASSICAL))
        self.socket_classical = client_socket_classical        

user0 = User("Alice", None, None, None) 
user1 = User("Bob", None, None, None)


def generate_Siftedkey(user0, user1, num_qubits):
    alice_bits = qrng(num_qubits)
    alice_basis = '0000011111'
    bob_basis = '0000011111'
    eve_basis = '1111111111'
    # alice_basis = qrng(num_qubits)
    # bob_basis = qrng(num_qubits)
    # eve_basis = qrng(num_qubits)

    # Alice generates qubits 
    qc = compose_quantum_circuit(num_qubits, alice_bits, alice_basis)

    # Eve eavesdrops Alice's qubits
    qc, eve_bits = intercept_resend(qc, eve_basis, intercept_prob=1.0)

    # Comparison their basis between Alice and Eve
    ae_basis, ae_match = check_bases(alice_basis, eve_basis)
    # Comparison their bits between Alice and Eve
    # ae_bits = check_bits(alice_bits,eve_bits,ae_basis)

    # Apply the quantum error channel
    # noise_model = apply_noise_model()

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

    # Alice sharekey
    alice_sharekey = ''
    # Bob sharekey
    bob_sharekey = ''

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
        # if ae_basis[i] == 'Y': # アリスとイヴ間で基底が一致
        #     ke += eve_bits[i]
        if ab_bits[i] == '!': # アリスとボブ間で基底は一致のはずだが、ビット値が異なる (イヴもしくはノイズによって、量子ビットの状態が変化)
            err_num += 1
    err_str = ''.join(['!' if ka[i] != kb[i] else ' ' for i in range(len(ka))])

    # print("Alice's remaining bits:                    " + ka)
    # print("Error positions (by Eve and noise):        " + err_str)
    # print("Bob's remaining bits:                      " + kb)

# Final key agreement process
# From here, it is a process of key reconciliation, but this approach will be implemented later.
# For the time being, currently, the shifted keys are compared with each other in a single function to generate a share key. (Only eliminating error bit positions in the comparison).

    sender_classical_channel.close()
    receiver_classical_channel.close()
        
    return ka, kb



def qrng(n):
    # generate n-bit string from measurement on n qubits using QuantumCircuit
    qc = QuantumCircuit(n,n)
    for i in range(n):
        qc.h(i) # The Hadamard gate has the effect of projecting a qubit to a 0 or 1 state with equal probability.
    qc.measure(list(range(n)),list(range(n)))
    # compiled_circuit = transpile(qc, backend)
    # result = backend.run(compiled_circuit, shots=1).result()
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


def compose_quantum_circuit(n, alice_bits, a) -> QuantumCircuit:
    qc = QuantumCircuit(n,n)
    qc.compose(encode_qubits(n, alice_bits, a), inplace=True)
    return qc


# def apply_noise_model():
#     p_meas = 0.01
#     error_meas = pauli_error([('X', p_meas), ('I', 1 - p_meas)])
#     noise_model = NoiseModel()
#     noise_model.add_all_qubit_quantum_error(error_meas, "measure")

#     return noise_model


def bob_measurement(qc,bob_basis):
    l = len(bob_basis)
    for i in range(l): 
        if bob_basis[i] == '1': # In case of Diagonal basis
            qc.h(i)

    qc.measure(list(range(l)),list(range(l))) 
    result = execute(qc,backend,shots=10).result() 
    counts = result.get_counts(0)
    max_key = max(counts, key=counts.get)
    bits = ''.join(list(reversed(max_key)))

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

def compare_bases(n, ab_bases, ab_bits, alice_bits, bob_bits):
    ka = ''  # kaの初期化
    kb = ''  # kbの初期化
    for i in range(n):
        if ab_bases[i] == 'Y':
            ka += alice_bits[i]
            kb += bob_bits[i]
    return ka, kb



# intercept Alice'squbits to measure and resend to Bob
def intercept_resend(qc,e, intercept_prob):
    backend = Aer.get_backend('qasm_simulator') 
    l = len(e)

    # num_to_intercept = int(l * intercept_prob)
    # to_intercept = random.sample(range(l), num_to_intercept)
    # print(to_intercept)

    # if len(to_intercept) < 1:
    #     return qc, None

    for i in range (l):
        if e[i] == '1':
            qc.h(i)

    # display(qc.draw())
    qc.measure(list(range(l)),list(range(l))) 
    result = execute(qc,backend,shots=1).result() 
    bits = list(result.get_counts().keys())[0] 
    bits = ''.join(list(reversed(bits)))

    qc.reset(list(range(l)))
    
    # イヴの情報を元に、アリスと同じエンコードをして、量子ビットの偏光状態を決める
    for i in range (l):
        if e[i] == '0':
            if bits[i] == '1':
                qc.x(i)
        else:
            if bits[i] == '0':
                qc.h(i)
            else:
                qc.x(i)
                qc.h(i)
    qc.barrier()
    # display(qc.draw())
    return [qc,bits]

# execute 1000 times
def main():
    error_rate = []
    for i in range(1000):
        correct = 0
        ka = ''
        kb = ''
        start = time.time()
        while(True):
            part_ka, part_kb = generate_Siftedkey(user0, user1, num_qubits_linux)
            ka += part_ka
            kb += part_kb
            if(len(ka) > sifted_key_length):
                mod = len(ka) % 7
                ka = ka[:len(ka)-mod]
                kb = kb[:len(kb)-mod]
                break

        reconciled_key_array = key_reconciliation_Hamming(ka, kb)
        reconciled_key = ''.join(map(str, map(int, reconciled_key_array)))
        end = time.time()

        for i in range(len(ka)):
            if int(ka[i]) != int(kb[i]):
                correct += 1

        # print(f'Error rate of sifted key: {(correct/len(ka))*100}')
        error_rate.append((correct/len(ka))*100)
        # print(f'Length of reconciled key: {len(reconciled_key)}')
        # print(f'Runtime: {end - start}')
        # print(f'Reconciled Key Rate: {len(reconciled_key)/(end-start)}')
    print(error_rate)

if __name__ == '__main__':
    main()

