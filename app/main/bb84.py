# ==================================================================================== #
# qkd/bb84.py

from sys import argv, exit
from qiskit import *
from qiskit import QuantumCircuit, Aer, execute
from random import seed, sample
from IPython.display import display

# local simulation
# backend = service.backend("simulator_mps")
backend = Aer.get_backend('qasm_simulator')
# simulator_mps
# backend = service.backend("ibmq_qasm_simulator")


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
def bob_measurement(qc,b):
    l = len(b)
    for i in range(l): 
        if b[i] == '1': 
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
    bb84 = QuantumCircuit(n,n)
    bb84.measure_all()
    bb84.compose(encode_qubits(n, alice_bits, a), inplace=True)
    return bb84


def compare_bases(n, ab_bases, ab_bits, alice_bits, bob_bits):
    ka = ''  # kaの初期化
    kb = ''  # kbの初期化
    for i in range(n):
        if ab_bases[i] == 'Y':
            ka += alice_bits[i]
            kb += bob_bits[i]
    return ka, kb

def channel(qc: QuantumCircuit) -> QuantumCircuit:
    # error rate
    # error_kraus = kraus_error([[[1, 0], [0, (1 - error_prob)**0.5]],
                        #   [[0, error_prob**0.5], [0, 0]]])
    # クラウス演算子を使用してノイズモデルを構築
    # 量子チャネルでのノイズによる量子情報の変化を再現
    # Reproducing changes in quantum information due to noise in the quantum channel.
    # noise_model = NoiseModel()
    # noise_model.add_quantum_error(error_kraus, 'x', list(len(n)))
    
    # transpiled_qc = transpile(qc, basis_gates=backend.configuration().basis_gates)
    # backend.run(transpiled_qc)

    return qc
