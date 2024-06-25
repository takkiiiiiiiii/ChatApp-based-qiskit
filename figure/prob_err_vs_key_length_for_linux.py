import numpy as np
import matplotlib.pyplot as plt

prob_err = np.array([1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99])
key_length = np.array([11.29, 10.20, 9.80, 8.54, 7.92, 6.43, 5.39, 5.19, 4.49, 2.42, 1.06, 0.09])

plt.figure(figsize=(8, 5))

plt.plot(prob_err, key_length, ls='-', marker='o')

plt.xlim(1, 100)
plt.ylim(0, 12)

plt.xticks(np.arange(0, 100, 5))
plt.yticks(np.arange(0, 12, 1))

plt.xlabel(r'Probability of error')
plt.ylabel(r'Sifted_Key_length')
plt.grid(alpha=0.3)

plt.title('Probability of error vs Key length (Generated Qubits = 22)')


plt.savefig('figure/prob_err_vs_key__length_for_linux.png', format='png', bbox_inches="tight", dpi=300)

plt.show()