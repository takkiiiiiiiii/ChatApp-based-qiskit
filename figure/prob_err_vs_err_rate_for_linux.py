import numpy as np
import matplotlib.pyplot as plt

qbit = np.array([1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99])
err_num = np.array([0.006642968142968144, 0.048651973026973036, 0.08868231768231767, 0.19700629925629923, 0.3214851325145442, 
0.37023711011210997, 0.4198132284382283, 0.6383777888777887, 0.6963432539682541, 0.7890240192813721, 0.8974145772528125, 0.9930375874125872])

plt.figure(figsize=(8, 5))

plt.plot(qbit, err_num, ls='-', marker='o')

plt.xlim(0, 100)
plt.ylim(0, 1)

plt.xticks(np.arange(0, 100, 5))
plt.yticks(np.arange(0, 1, 0.1))

plt.xlabel(r'Probability of error')
plt.ylabel(r'Number of errors')
plt.grid(alpha=0.3)

plt.title('Probability of Error vs Error_rate (Generated Qubits = 22)')

plt.savefig('figure/prob_err_vs_err_rate_for_linux.png', format='png', bbox_inches="tight", dpi=300)

plt.show()