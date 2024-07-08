import numpy as np
import matplotlib.pyplot as plt

qbit = np.array([1, 5, 10, 15, 20, 25])
Runtime = np.array([165.3557719979093, 161.9371129189411, 149.17373979531592, 124.00209025385817,
                    99.57256148432295, 70.21376954982021])

plt.figure(figsize=(8, 5))

plt.plot(qbit, Runtime, ls='-', marker='o')

plt.xlim(0, 26)
plt.ylim(69, 170)

plt.yticks(np.arange(70, 170, 10))
plt.xticks(np.arange(0, 26, 5))

plt.xlabel(r'Noise Incidence Rate')
plt.ylabel(r'Reconcilied Key Rate')
plt.grid(alpha=0.3)

plt.savefig('noise_vs_reconcilied_keyrate.png', format='png', bbox_inches="tight", dpi=300)

plt.show()