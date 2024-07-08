import numpy as np
import matplotlib.pyplot as plt

qbit = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

KeyRate = np.array([20.232040298056823, 43.34172585992227, 57.72803576225145, 71.51974370100983, 88.04862552436444, 102.70040940059015, 116.85576384707154, 
                    128.64652098156, 144.77341622715605 ,157.97296367832598, 160.55000058348247, 162.9478449057025, 156.8276186385533, 148.82918502748132, 
                    76.04067635369164, 63.68143525427732, 55.02481178233751, 36.47027382616829, 17.763042791025274, 9.993452217300653, 5.116103720164548, 
                    2.8057342202369617, 1.421838490249446, 0.7129057861527669])

Runtime = np.array([0.02770237684249878, 0.02807220220565796, 0.028750681877136232, 0.029110944271087645,
                    0.029559779167175292, 0.030656797885894774, 0.032105517387390134, 0.032907323837280275,
                    0.03253787040710449, 0.03461364507675171, 0.0360117769241333, 0.03796216011047363,
                    0.040640277862548826, 0.047282912731170655, 0.11713955640792846, 0.12335862636566162,
                    0.16416435956954956, 0.24074086904525757, 0.45067141771316527, 0.9586353850364685,
                    1.9109086751937867, 3.8275503635406496, 8.607606101036072, 16.79662356376648])

fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:blue'
ax1.set_xlabel('Generated Qubits from IBM Platform per execution', fontsize=14)
ax1.set_ylabel('Sifted Key Rate (bps)', color=color, fontsize=14)
ax1.plot(qbit, KeyRate, color=color, marker='o', label='Sifted Key Rate (bps)')
ax1.tick_params(axis='y', labelcolor=color, labelsize=12)
ax1.tick_params(axis='x', labelsize=12)
ax1.set_ylim(0, 165)
ax1.set_xlim(0, 24.5)
ax1.set_xticks(np.arange(0, 25, 1))
ax1.set_yticks(np.arange(0, 170, 10))
ax1.grid(alpha=0.3)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Runtime (s)', color=color, fontsize=14)
ax2.plot(qbit, Runtime, color=color, marker='o', label='Runtime (s)')
ax2.tick_params(axis='y', labelcolor=color, labelsize=12)
ax2.set_ylim(0, 10)
ax2.set_yticks(np.arange(0, 11, 1))
ax2.grid(alpha=0.3)

fig.suptitle('Generated Qubits from IBM Platform per Execution vs. Sifted Key Rate and Runtime')
fig.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.savefig('qlength_vs_keyrate_runtime.png', format='png', bbox_inches="tight", dpi=300)

plt.show()
