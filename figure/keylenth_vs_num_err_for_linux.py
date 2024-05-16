import numpy as np
import matplotlib.pyplot as plt

prob_err = np.array([1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99])
key_length = np.array([10.85, 9.89, 9.28, 7.59, 6.27, 5.85, 5.46, 5.94, 6.10, 7.59, 8.98, 10.61])

plt.figure(figsize=(8, 5))

plt.plot(prob_err, key_length, ls='-', marker='o')

plt.xlim(1, 110)
plt.ylim(4, 11)

plt.xticks(np.arange(0, 110, 5))
plt.yticks(np.arange(4, 11, 1))

plt.xlabel(r'Probability of error')
plt.ylabel(r'Key_length')
plt.grid(alpha=0.3)

plt.title('Key length vs Number of Errors (Generated Qubits = 22)')


plt.savefig('figure/keylength_vs_num__err_for_linux.png', format='png', bbox_inches="tight", dpi=300)

plt.show()