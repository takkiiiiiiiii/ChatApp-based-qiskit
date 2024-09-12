import numpy as np
import matplotlib.pyplot as plt

qbit = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
Runtime = np.array([20.232040298056823, 43.34172585992227, 57.72803576225145, 71.51974370100983, 88.04862552436444, 102.70040940059015, 116.85576384707154, 
                    128.64652098156, 144.77341622715605 ,157.97296367832598, 160.55000058348247, 162.9478449057025])

plt.figure(figsize=(8, 5))

plt.plot(qbit, Runtime, ls='-', marker='o')

plt.xlim(0, 12.5)
plt.ylim(0, 165)

plt.yticks(np.arange(0, 165, 10))
plt.xticks(np.arange(0, 12.5, 1))

plt.xlabel(r'Generated Qubits from IBM Platform per a execution')
plt.ylabel(r'Sifted Key rate(bps)')
plt.grid(alpha=0.3)

plt.savefig('qlength_vs_keyrate3.png', format='png', bbox_inches="tight", dpi=300)

plt.show()