import numpy as np
import matplotlib.pyplot as plt

qbit = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
Runtime = np.array([0.02770237684249878, 0.02807220220565796, 0.028750681877136232, 0.029110944271087645,
                    0.029559779167175292, 0.030656797885894774, 0.032105517387390134, 0.032907323837280275,
                    0.03253787040710449, 0.03461364507675171, 0.0360117769241333, 0.03796216011047363,
                    0.040640277862548826, 0.047282912731170655, 0.11713955640792846, 0.12335862636566162,
                    0.16416435956954956, 0.24074086904525757, 0.45067141771316527, 0.9586353850364685,
                    1.9109086751937867, 3.8275503635406496, 8.607606101036072, 16.79662356376648])

plt.figure(figsize=(8, 5))

plt.plot(qbit, Runtime, ls='-', marker='o')

plt.xlim(0, 24.5)
plt.ylim(0, 10)

plt.yticks(np.arange(0, 10, 1))
plt.xticks(np.arange(0, 24.5, 1))

plt.xlabel(r'Generated Qubits from IBM Platform per a execution')
plt.ylabel(r'Runtime(s)')
plt.grid(alpha=0.3)

plt.savefig('qlength_vs_runtime.png', format='png', bbox_inches="tight", dpi=300)

plt.show()