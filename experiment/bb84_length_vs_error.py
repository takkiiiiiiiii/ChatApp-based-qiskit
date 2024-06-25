from sys import argv, exit
from qiskit import QuantumCircuit, Aer, execute
from qiskit_aer.noise import (NoiseModel, QuantumError, pauli_error, depolarizing_error)
from IPython.display import display



count = 100
total = 0
len_key = 2048
num_qubit_linux = 12 # for Linux
num_qubit_mac = 24 # for mac
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

user0 = User("Alice", any, any, any) 
user1 = User("Bob", any, any, any)

def bb84(user0, user1, num_qubits, len_key):
    alice_bits = qrng(num_qubits)
    alice_basis = qrng(num_qubits)
    bob_basis = qrng(num_qubits)
    eve_basis = qrng(num_qubits)

    # Alice generates qubits 
    qc = compose_quantum_circuit(num_qubits, alice_bits, alice_basis)

    # Eve intercepts Alice's qubits and resends to Bob
    # qc, eve_bits = intercept_resend(qc, eve_basis)

    # Comparison their basis between Alice and Eve
    ae_basis, ae_match = check_bases(alice_basis, eve_basis)
    # Comparison their bits between Alice and Eve
    # ae_bits = check_bits(alice_bits,eve_bits,ae_basis)
    
    # Bob measure Alice's qubit
    qc, bob_bits = bob_measurement(qc, bob_basis, num_qubits)

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
        if ab_bits[i] == '!': # アリスとボブ間で基底は一致のはずだが、ビット値が異なる (due to noise in quantum channel or eavesdropping)
            err_num += 1
    err_str = ''.join(['!' if ka[i] != kb[i] else ' ' for i in range(len(ka))])

    print("Alice's sifted keys:                       " + ka)
    print("Error positions (by Eve and noise):        " + err_str)
    print("Bob's sifted keys:                         " + kb)

# Final key agreement process

# From here, it is a process of key reconciliation, but this approach will be implemented later.
# For the time being, currently, the shifted keys are compared with each other in a single function to generate a share key. (Only eliminating error bit positions in the comparison).

    for i in range(len(ka)):
        if ka[i] == kb[i]:
            alice_sharekey += ka[i]
            bob_sharekey += kb[i]
    
    sender_classical_channel.close()
    receiver_classical_channel.close()
        
    print("Alice's sharekey ", alice_sharekey)
    print("Bob's sharekey ", bob_sharekey)

    sharekey_length = len(alice_sharekey)
    siftedkey_length = len(ka)

    return err_num, siftedkey_length, sharekey_length


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
    counts = result.get_counts(0)
    max_key = max(counts, key=counts.get)
    bits = ''.join(list(reversed(max_key))) 
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


# b = Bob's basis infomation
# Bob has some error by noise. That means that his sequence of bit is different from Alice's 
def bob_measurement(qc,b, num_qubits):
    l = len(b)
    for i in range(l): 
        if b[i] == '1': # In case of Diagonal basis
            qc.h(i)

    p_meas = 0.1 # Probability of error
    error_meas = pauli_error([('X', p_meas), ('I', 1 - p_meas)])
    noise_model = NoiseModel()
    noise_model.add_all_qubit_quantum_error(error_meas, "measure")

    qc.measure(list(range(l)),list(range(l))) 
    result = execute(qc,backend,shots=10, noise_model=noise_model).result() 
    # result = execute(qc,backend,shots=1).result()

    # bits = list(result.get_counts().keys())[0]
    # bits = ''.join(list(reversed(bits)))
    counts = result.get_counts(0)
    max_key = max(counts, key=counts.get)
    # bits = counts.most_frequent()
    bits = ''.join(list(reversed(max_key)))
    print("Bob bits: " + bits)

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
    # qc.measure_all()
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

    qc.measure(list(range(l)),list(range(l))) 
    result = execute(qc,backend,shots=1).result() 
    counts = result.get_counts(0)
    max_key = max(counts, key=counts.get)
    # bits = list(result.get_counts().keys())[0] 
    bits = ''.join(list(reversed(max_key)))

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
    return [qc,bits]


# execute 1000 times




def main():
    total_err_rate = 0
    total_err_num = 0
    total_sharekey_length = 0
    for i in range(count):
        err_num, siftedkey_length, sharekey_length = bb84(user0, user1, num_qubit_linux, len_key)
        print("Nmber of Errors to generate share key: ", err_num, "\n\n")
        total_err_num += err_num
        # Calculate Error rate
        err_rate = err_num / siftedkey_length
        total_err_rate += err_rate
        total_sharekey_length += sharekey_length

    ave_err_rate = total_err_rate / count
    ave_err_num = total_err_num / count
    ave_key_length = total_sharekey_length / count
    print(f'Average error rate to generate the sharekey ({count} times); {ave_err_rate}\n\n')
    print(f'Average number of error to generate the sharekey ({count} times); {ave_err_num}\n\n')
    print(f'Average number of Key length ({count} times); {ave_key_length}\n\n')


if __name__ == '__main__':
    main()
