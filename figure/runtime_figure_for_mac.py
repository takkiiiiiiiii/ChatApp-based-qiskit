import numpy as np
import matplotlib.pyplot as plt

qbit = np.array([24, 25, 26, 27, 28, 29])
Runtime = np.array([0.302937, 0.312837, 0.321039, 0.328847, 0.334705, 0.352969])

plt.figure(figsize=(8, 5))

plt.plot(qbit, Runtime, ls='-', marker='o')

plt.xlim(24, 30)
plt.ylim(0, 0.5)

plt.yticks(np.arange(0, 0.5, 0.1))
plt.xticks(np.arange(24, 30, 1))

plt.xlabel(r'Number of Generated Qubit')
plt.ylabel(r'Runtime(s)')
plt.grid(alpha=0.3)

plt.savefig('runtime_for_mac.png', format='png', bbox_inches="tight", dpi=300)

plt.show()