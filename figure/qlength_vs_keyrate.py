import numpy as np
import matplotlib.pyplot as plt

qbit = np.array([17, 18, 19, 20, 21, 22, 23])
Runtime = np.array([0.63694, 0.96880, 1.89293, 9.515962520415792, 5.116103720164548, 2.8057342202369617, ])

plt.figure(figsize=(8, 5))

plt.plot(qbit, Runtime, ls='-', marker='o')

plt.xlim(19, 26)
plt.ylim(-1, 16)

plt.yticks(np.arange(0, 16, 2))
plt.xticks(np.arange(20, 26, 1))

plt.xlabel(r'Number of Generated Qubit')
plt.ylabel(r'Runtime(s)')
plt.grid(alpha=0.3)

plt.savefig('key_length_vs_runtime.png', format='png', bbox_inches="tight", dpi=300)

plt.show()