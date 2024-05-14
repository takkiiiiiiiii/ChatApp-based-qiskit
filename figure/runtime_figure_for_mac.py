# import numpy as np
# import matplotlib.pyplot as plt


# qbit = np.array([10, 20, 40, 60, 80, 100])
# key_size = np.array([4, 8, 16, 22, 28, 35])

# plt.figure(figsize=(9,5.5))

# plt.plot(qbit, key_size, ls='-', marker='o', markersize=7)

# plt.xlim(10, 100)
# plt.ylim(0, 35)

# plt.yticks(np.arange(5, 37, 5), fontsize=18)
# plt.xticks(np.arange(20, 101, 20), fontsize=18)

# plt.xlabel(r'Number of Generated Qubit', fontsize=23)
# plt.ylabel(r'Key size (bits)', fontsize=23)
# plt.grid()

# plt.savefig('Yudai_figure.png', format='png', bbox_inches="tight")

# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt


# qbit = np.array([20, 21, 22, 23, 24, 25])
# key_size = np.array([0, 1, 3, 6, 10, 15])

# plt.figure(figsize=(4,2.5))

# plt.plot(qbit, key_size, ls='-', marker='o')

# plt.xlim(8, 102)
# plt.ylim(-1, 36)

# plt.yticks(np.arange(5, 37, 5))
# plt.xticks(np.arange(20, 101, 20))

# plt.xlabel(r'Number of Generated Qubit')
# plt.ylabel(r'Key size (bits)')
# plt.grid(alpha=0.3)

# plt.savefig('Yudai_figure.png', format='png', bbox_inches="tight", dpi=600)

# plt.show()

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

plt.savefig('run_time_for_mac.png', format='png', bbox_inches="tight", dpi=300)

plt.show()