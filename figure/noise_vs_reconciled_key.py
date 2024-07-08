import numpy as np
import matplotlib.pyplot as plt


noise = np.array([1, 5, 10, 15, 20, 25])
Key_rate = np.array([165.3557719979093, 161.9371129189411, 149.17373979531592,
                     124.56273947531164, 99.57256148432295, 71.8592312233456])

plt.figure(figsize=(8, 5))

plt.plot(noise, Key_rate, ls='-', marker='o')


plt.xlim(0, 25.5)
plt.ylim(70, 170)

plt.yticks(np.arange(70, 170, 10))
plt.xticks(np.arange(0, 25.5, 5))

plt.xlabel(r'Noise Incidence Rate')
plt.ylabel(r'Reconcilied Key Rate')
plt.grid(alpha=0.3)

plt.savefig('noise_vs_reconcilied_keyrate.png', format='png', bbox_inches="tight", dpi=300)

plt.show()