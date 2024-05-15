from qiskit import QuantumCircuit, execute
from qiskit_aer import Aer
from qiskit.tools.visualization import plot_histogram
from qiskit_aer.noise import (NoiseModel, QuantumError, pauli_error, depolarizing_error)

backend = Aer.get_backend('qasm_simulator')
qc = QuantumCircuit(4)

p_meas = 0.01

error_meas = pauli_error([('X', p_meas), ('I', 1 - p_meas)])

noise_model = NoiseModel()
noise_model.add_all_qubit_quantum_error(error_meas, "measure")

qc.measure_all()
result = execute(qc,backend,shots=1000, noise_model=noise_model).result() 
# result = execute(qc,backend,shots=1000).result() 

counts = result.get_counts(0)
plot_histogram(counts)
bits = list(result.get_counts(0).keys())[0]

print(bits)
print(noise_model)
# print(counts)