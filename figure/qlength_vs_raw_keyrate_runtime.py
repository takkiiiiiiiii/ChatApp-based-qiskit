import numpy as np
import matplotlib.pyplot as plt

qbit = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])

raw_keyrate = np.array([34.17625904008257,
                        66.76432794012169,
                        98.80941826762381,
                        127.26977235601807,
                        155.18522730032552,
                        183.80680518767824,
                        213.19401780365854,
                        238.754178219528,
                        263.77385469064257,
                        289.7481174509968,
                        311.95919306318007,
                        335.50457615113197,
                        353.069874229099,
                        368.0363931165903,
                        354.20864139657354,
                        331.5325230612613,
                        277.1300421912454,
                        260.23354870257367,
                        244.326050067844,
                        237.1622233043871,
                        206.78943947847924,
                        170.56794240172917,
                        95.40042936328724,
                        51.26175335246058,
                        27.121244636048225,
                        14.06286828175562,
                        9.163440955369921,
                        5.029635853865307])



runtime = np.array([0.030648962497711183,
                    0.031190741062164306,
                    0.031429704189300536,
                    0.03256327795982361,
                    0.03337643218040466,
                    0.033726511240005495,
                    0.033779738426208496,
                    0.03454101538658142,
                    0.035104369163513185,
                    0.03546370887756348,
                    0.036264004945755005,
                    0.03668445825576782,
                    0.03779942512512207,
                    0.03904728436470032,
                    0.07095387578010559,
                    0.08424869012832642,
                    0.07281828355789184,
                    0.08893818235397338,
                    0.10205545330047608,
                    0.10819197297096253,
                    0.09783755159378052,
                    0.1314389853477478,
                    0.24261543345451356,
                    0.47752925848960875,
                    0.9473192849159241,
                    1.9476069226264954,
                    3.8414738085269926,
                    7.612790372133255])

fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:blue'
ax1.set_xlabel('Generated Qubits from IBM Platform per execution', fontsize=22)
ax1.set_ylabel('Raw Key Rate (qubit/second)', color=color, fontsize=22)
ax1.plot(qbit, raw_keyrate, color=color, marker='o', label='Sifted Key Rate (bps)', markersize=10)
ax1.tick_params(axis='y', labelcolor=color, labelsize=22)
ax1.tick_params(axis='x', labelsize=20)
ax1.set_ylim(0, 400)
ax1.set_xlim(0, 29)
ax1.set_xticks(np.arange(0, 29, 2))
ax1.set_yticks(np.arange(0, 401, 50))
ax1.grid(alpha=0.3)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Execution time(s)', color=color, fontsize=22)
ax2.plot(qbit, runtime, color=color, marker='s', label='Runtime (s)', markersize=10)
ax2.tick_params(axis='y', labelcolor=color, labelsize=22)
ax2.set_ylim(0, 8)
ax2.set_yticks(np.arange(0, 8, 1))
ax2.grid(alpha=0.3)

# fig.suptitle('Generated Qubits from IBM Platform per Execution vs. Sifted Key Rate and Runtime')
fig.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.savefig('qlength_vs_raw_sifted_keyrate.png', format='png', bbox_inches="tight", dpi=300)

plt.show()



