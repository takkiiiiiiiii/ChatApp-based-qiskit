import numpy as np
import matplotlib.pyplot as plt

qbit = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
Runtime = np.array([20.232040298056823, 43.34172585992227, 57.72803576225145, 71.51974370100983, 88.04862552436444, 102.70040940059015, 116.85576384707154, 
                    128.64652098156, 144.77341622715605 ,157.97296367832598, 160.55000058348247, 162.9478449057025, 156.8276186385533, 148.82918502748132, 
                    76.04067635369164, 63.68143525427732, 55.02481178233751, 36.47027382616829, 17.763042791025274, 9.993452217300653, 5.116103720164548, 
                    2.8057342202369617, 1.421838490249446, 0.7129057861527669])

plt.figure(figsize=(8, 5))

plt.plot(qbit, Runtime, ls='-', marker='o')

plt.xlim(0, 24.5)
plt.ylim(0, 165)

plt.yticks(np.arange(0, 165, 10))
plt.xticks(np.arange(0, 24.5, 1))

plt.xlabel(r'Generated Qubits from IBM Platform per a execution')
plt.ylabel(r'Sifted Key rate(bps)')
plt.grid(alpha=0.3)

plt.savefig('qlength_vs_keyrate.png', format='png', bbox_inches="tight", dpi=300)

plt.show()