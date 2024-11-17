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


sifted_keyrate = np.array([17.975377202092158,
                           32.646282651675975,
                           49.27948128893049,
                           63.19507494857445,
                           77.84953760829212,
                           89.80146740208069,
                           107.42824224694955,
                           118.81277640090873,
                            134.08318398062679,
                            144.64017113857255,
                            157.55492711364775,
                            166.05948037165567,
                            176.59514588876203,
                            184.28578137640417,
                            178.27077743901515,
                            166.8860382533602,
                            138.750983595191,
                            130.35426358456013,
                            121.6571549759994,
                            120.73837215745445,
                            103.11900602036204,
                            86.33804102821925,
                            47.43018652189507,
                            25.839873586487364,
                            13.626736762482436,
                            7.041239405981448,
                            4.730528923193832,
                            2.4888060050044127])

fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:blue'
ax1.set_xlabel('Generated Qubits from IBM Platform per execution', fontsize=22)
ax1.set_ylabel('Raw Key Rate (bps)', color=color, fontsize=22)
ax1.plot(qbit, raw_keyrate, color=color, marker='o', label='Sifted Key Rate (bps)', markersize=10)
ax1.tick_params(axis='y', labelcolor=color, labelsize=22)
ax1.tick_params(axis='x', labelsize=20)
ax1.set_ylim(0, 410)
ax1.set_xlim(0, 29)
ax1.set_xticks(np.arange(0, 29, 2))
ax1.set_yticks(np.arange(0, 410, 50))
ax1.grid(alpha=0.3)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Sifted Key Rate (bps)', color=color, fontsize=22)
ax2.plot(qbit, sifted_keyrate, color=color, marker='s', label='Runtime (s)', markersize=10)
ax2.tick_params(axis='y', labelcolor=color, labelsize=22)
ax2.set_ylim(0, 410)
ax2.set_yticks(np.arange(0, 410, 50))
ax2.grid(alpha=0.3)

# fig.suptitle('Generated Qubits from IBM Platform per Execution vs. Sifted Key Rate and Runtime')
fig.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.savefig('qlength_vs_raw_sifted_keyrate.png', format='png', bbox_inches="tight", dpi=300)

plt.show()
