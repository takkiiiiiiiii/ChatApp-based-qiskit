import numpy as np
import matplotlib.pyplot as plt

qbit = np.array([1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99])
err_num = np.array([0.19, 1.14, 2.0, 3.66, 4.46, 5.26, 5.39, 5.09, 4.80, 3.56, 1.89, 0.28])

plt.figure(figsize=(8, 5))

plt.plot(qbit, err_num, ls='-', marker='o')

plt.xlim(1, 100)
plt.ylim(0, 6)

plt.xticks(np.arange(0, 110, 5))
plt.yticks(np.arange(0, 6, 0.5))

plt.xlabel(r'Probability of error')
plt.ylabel(r'Number of errors')
plt.grid(alpha=0.3)

plt.title('Probability of Error vs Number of Errors (Generated Qubits = 22)')

plt.savefig('figure/prob_err_vs_num_err_for_linux.png', format='png', bbox_inches="tight", dpi=300)

plt.show()