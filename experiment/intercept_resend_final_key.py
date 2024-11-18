from qiskit import QuantumCircuit, Aer, execute
from qiskit_aer.noise import (NoiseModel, QuantumError, pauli_error, depolarizing_error)
from kr_Hamming import key_reconciliation_Hamming
from IPython.display import display
from qiskit.tools.visualization import plot_histogram
import numpy as np
import random
import math
import time



count = 1000
sifted_key_length = 1000
num_qubits_linux = 14 # for Linux
num_qubits_mac = 19 # for mac
backend = Aer.get_backend('qasm_simulator')
noise_prob_range = [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]
intercept_prob_range = [0, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1]
p_estimation = 0.25
sifting_coefficiant = 0.5
kr_efficiency = 1.22 

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



def generate_Siftedkey(user0, user1, num_qubits, intercept_prob, noise_prob):
    start = time.time()
    alice_bits = qrng(num_qubits)
    alice_basis = qrng(num_qubits)
    bob_basis = qrng(num_qubits)
    eve_basis = qrng(num_qubits)

    # Alice generates qubits
    qc = compose_quantum_circuit(num_qubits, alice_bits, alice_basis)

    # Quantum Circuit for Eve
    qc2 = compose_quantum_circuit_for_eve(num_qubits, alice_bits, alice_basis)

    # Eve eavesdrops Alice's qubits
    qc, eve_basis, eve_bits = intercept_resend(qc, qc2, eve_basis, intercept_prob)

    # Comparison their basis between Alice and Eve
    ae_basis, ae_match = check_bases(alice_basis, eve_basis)
    # Comparison their bits between Alice and Eve
    # ae_bits = check_bits(alice_bits,eve_bits,ae_basis)

    # Apply the quantum error chanel
    noise_model = apply_noise_model(noise_prob)

    # Bob measure Alice's qubit
    qc, bob_bits = bob_measurement(qc,bob_basis,noise_model)

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
    ke= eve_bits
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
            # ke += eve_bits[i]
        if ab_bits[i] == '!': # アリスとボブ間で基底は一致のはずだが、ビット値が異なる (イヴもしくはノイズによって、量子ビットの状態が変化)
            err_num += 1
    err_str = ''.join(['!' if ka[i] != kb[i] else ' ' for i in range(len(ka))])

    end = time.time()
    runtime = end - start

    # print("Alice's remaining bits:                    " + ka)
    # print("Error positions (by Eve and noise):        " + err_str)
    # print("Bob's remaining bits:                      " + kb)

# Final key agreement process
# From here, it is a process of key reconciliation, but this approach will be implemented later.
# For the time being, currently, the shifted keys are compared with each other in a single function to generate a share key. (Only eliminating error bit positions in the comparison).

    sender_classical_channel.close()
    receiver_classical_channel.close()
    # print("eve_basis: ", eve_basis)

    error_num = 0
    for i in range(len(ka)):
        if ka[i] != kb[i]:
            error_num += 1
    
    return ka, kb, runtime, error_num


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

# AliceとBobがビット値を生成するための量子回路
def compose_quantum_circuit(num_qubit, alice_bits, alice_basis) -> QuantumCircuit:
    qc = QuantumCircuit(num_qubit, num_qubit)
    qc.compose(encode_qubits(num_qubit, alice_bits, alice_basis), inplace=True)
    return qc


# qcと同じ実装だが、イブのビット値を生成するための量子回路
def compose_quantum_circuit_for_eve(num_qubit, alice_bits, alice_basis) -> QuantumCircuit:
    qc2 = QuantumCircuit(num_qubit, num_qubit)
    qc2.compose(encode_qubits(num_qubit, alice_bits, alice_basis), inplace=True)
    return qc2


def apply_noise_model(p_meas):
    error_meas = pauli_error([('X', p_meas), ('I', 1 - p_meas)])
    noise_model = NoiseModel()
    noise_model.add_all_qubit_quantum_error(error_meas, "measure")

    return noise_model


def bob_measurement(qc,bob_basis,noise_model):
    l = len(bob_basis)
    for i in range(l): 
        if bob_basis[i] == '1': # In case of Diagonal basis
            qc.h(i)

    qc.measure(list(range(l)),list(range(l))) 
    # result = execute(qc,backend,shots=10, noise_model=noise_model).result() 
    result = execute(qc,backend,shots=1, noise_model=noise_model).result() 
    counts = result.get_counts(0)
    max_key = max(counts, key=counts.get)
    bits = ''.join(list(reversed(max_key)))

    # display(qc.draw())
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
def intercept_resend(qc, qc2, eve_basis , intercept_prob):
    backend = Aer.get_backend('qasm_simulator')

    l = len(eve_basis)
    num_to_intercept = int(num_qubits_linux * intercept_prob)
    to_intercept = random.sample(range(num_qubits_linux), num_to_intercept)
    to_intercept = sorted(to_intercept)
    # print(to_intercept)
    eve_basis = list(eve_basis)

    for i in range(len(eve_basis)):
        if i not in to_intercept:
            eve_basis[i] = '!'

    # print(f"Eve basis: {len(eve_basis)}")

    for i in to_intercept:
        if eve_basis[i] == '1':
            qc.h(i)
            qc2.h(i)

    qc2.measure(list(range(l)),list(range(l))) 
    result = execute(qc2,backend,shots=1).result() 
    bits = list(result.get_counts().keys())[0] 
    bits = ''.join(list(reversed(bits)))

    # qc.reset(list(range(l)))
    
    # イヴの情報を元に、アリスと同じエンコードをして、量子ビットの偏光状態を決める
    for i in range (l):
        if eve_basis[i] == '0':
            if bits[i] == '1':
                qc.x(i)
        elif eve_basis[i] == '1':
            if bits[i] == '0':
                qc.h(i)
            else:
                qc.x(i)
                qc.h(i)

    # display(qc.draw())
    qc.barrier()

    return [qc, eve_basis ,bits]

# execute 1000 times
# Derive the final key rate
def main():
    # noise_prob = 0.07
    # intercept_prob = 0.6
    qber = 0
    zero = 0
    final_keyrate = 0
    total_qber = 0
    total_final_keyrate = 0
    total_raw_keyrate = 0
    print(F"Number of Qubits: {num_qubits_linux}")
    for noise_prob in noise_prob_range: # channel noise
        for intercept_prob in intercept_prob_range:
            print(f"Channel Noise Ratio:             {noise_prob*100}%")
            print(f"Intercept-and-resend Ratio:      {intercept_prob*100}%")
            for i in range(count):
                ka, kb, execution_time, error_num = generate_Siftedkey(user0, user1, num_qubits_linux, intercept_prob, noise_prob)
                if len(ka) == 0:
                    zero += 1
                    continue
                raw_keyrate = num_qubits_linux / execution_time
                total_raw_keyrate += raw_keyrate
                qber = error_num / len(ka)
                total_qber += qber
            # total_raw_keyrate /= (count-zero)
            # total_qber /= (count-zero)
            if total_qber / (count-zero) == 0:
                ab_entropy = 0
            else:
                qber = total_qber / (count-zero) # update qber variable 
                # print(f"qber : {qber}")
                # print(f"Raw key rate: {raw_keyrate}")
                ab_entropy = -qber*math.log2(qber)-(1-qber)*math.log2(1-qber)
            ae_entropy = 1-ab_entropy
            # raw_keyrate = total_raw_keyrate / (count-zero) # update raw_keyrate variable 
            raw_keyrate = 368.0363931165903 # the raw key rate in case of 14 qubits (Average of 10000 times runs)
            final_keyrate = raw_keyrate*sifting_coefficiant*p_estimation*(ae_entropy-kr_efficiency*ab_entropy)
            print(f"Average of QBER({count-zero}times):   {(total_qber/(count-zero))*100} %")
            print(f"Average of Raw Key Rate({count-zero}times):   {total_raw_keyrate/(count-zero)} (pulse/second)")
            print(f"Final Key Rate:   {final_keyrate} (bps)")
            print("\n")
            qber = 0
            zero = 0
            total_qber = 0
            total_raw_keyrate = 0
    

    # print(f'Final Key Rate (average of {count}):  {total_keyrate / count}')
    # print(f"QBER (average of {count}):             {total_qber/count}")

if __name__ == '__main__':
    main()