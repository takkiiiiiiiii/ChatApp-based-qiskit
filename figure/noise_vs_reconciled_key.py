import numpy as np
import matplotlib.pyplot as plt

qbit = np.array([1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99])
Runtime = np.array([165.3557719979093, 161.9371129189411, 149.17373979531592, 
                    99.57256148432295, 55.03459383695526, 30.084042544188403, 
                    16.430760997467242, 2.211899916937343, 0, 0, 0, 0])

plt.figure(figsize=(8, 5))

plt.plot(qbit, Runtime, ls='-', marker='o')

plt.xlim(1, 100)
plt.ylim(0, 170)

plt.yticks(np.arange(0, 170, 10))
plt.xticks(np.arange(1, 100, 10))

plt.xlabel(r'Probability of error')
plt.ylabel(r'Reconcilied Key Rate')
plt.grid(alpha=0.3)

plt.savefig('noise_vs_reconcilied_keyrate.png', format='png', bbox_inches="tight", dpi=300)

plt.show()