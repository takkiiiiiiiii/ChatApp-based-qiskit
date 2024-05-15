import numpy as np
import matplotlib.pyplot as plt

qbit = np.array([20, 21, 22, 23, 24, 25, 26])
Runtime = np.array([0.514803249835968, 0.6059057593345643, 0.8416175055503845,
3.069843992471695, 3.5662420630455016, 6.648118734359741, 12.616631937026977])

plt.figure(figsize=(8, 5))

plt.plot(qbit, Runtime, ls='-', marker='o')

plt.xlim(19, 27)
plt.ylim(-1, 16)

plt.yticks(np.arange(0, 16, 2))
plt.xticks(np.arange(20, 26, 1))

plt.xlabel(r'Number of Generated Qubit')
plt.ylabel(r'Runtime(s)')
plt.grid(alpha=0.3)

plt.savefig('runtime_for_linux.png', format='png', bbox_inches="tight", dpi=300)

plt.show()