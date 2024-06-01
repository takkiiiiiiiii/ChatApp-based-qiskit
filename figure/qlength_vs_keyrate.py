import numpy as np
import matplotlib.pyplot as plt

qbit = np.array([18, 19, 20, 21, 22, 23, 24])
Runtime = np.array([34.55332735179009, 18.79876542729929, 9.515962520415792, 5.116103720164548, 2.8057342202369617, 1.421838490249446, 0.7129057861527669])

plt.figure(figsize=(8, 5))

plt.plot(qbit, Runtime, ls='-', marker='o')

plt.xlim(18, 24.5)
plt.ylim(0, 35)

plt.yticks(np.arange(0, 35, 2))
plt.xticks(np.arange(18, 24.5, 1))

plt.xlabel(r'Number of Generated Qubit')
plt.ylabel(r'Key rate(bps)')
plt.grid(alpha=0.3)

plt.savefig('key_length_vs_runtime.png', format='png', bbox_inches="tight", dpi=300)

plt.show()