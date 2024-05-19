import numpy as np
import matplotlib.pyplot as plt

qbit = np.array([1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99])
err_num = np.array([0.07, 0.54, 0.97, 2.08, 3.43, 4.14, 4.74, 6.61, 7.67, 8.91, 9.81, 10.74])

plt.figure(figsize=(8, 5))

plt.plot(qbit, err_num, ls='-', marker='o')

plt.xlim(0, 100)
plt.ylim(0, 11)

plt.xticks(np.arange(0, 100, 5))
plt.yticks(np.arange(0, 11, 0.5))

plt.xlabel(r'Probability of error')
plt.ylabel(r'Number of errors')
plt.grid(alpha=0.3)

plt.title('Probability of Error vs Number of Errors (Generated Qubits = 22)')

plt.savefig('figure/prob_err_vs_num_err_for_linux.png', format='png', bbox_inches="tight", dpi=300)

plt.show()