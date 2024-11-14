import numpy as np
import matplotlib.pyplot as plt

qbit = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])

raw_keyrate = np.array([38.54732985189226,
                        74.24575714759764,
                        107.59079527074378,
                        142.76880545668163,
                        178.89366983814946,
                        207.7372605018291,
                        236.20693135534194,
                        269.6245347027024,
                        295.8939803332242,
                        325.0035932394877,
                        353.7705262585217,
                        387.9116099739265,
                        416.37226856956505,
                        439.46353986006403,
                        462.70730627124885,
                        485.74762315239474,
                        513.8991492581732,
                        549.6843579445367,
                        563.9864827122987,
                        588.6683461971203,
                        600.8241818531283,
                        631.1509023906881,
                        659.0640375594196,
                        678.0934634802047,
                        713.956280673055,
                        727.5036016688168,
                        755.6669542327801,
                        770.2945141517595,
                        796.7281640091168])



sifted_keyrate = np.array([19.560515287165643,
                            35.50330785958951,
                            54.4065618416693,
                            69.34066480873358,
                            89.18927435836389,
                            103.7872462423986,
                            118.17585249858467,
                            130.63124212512716,
                            148.6424564290608,
                            161.99361681428903,
                            176.52054603310864,
                            195.7651730641794,
                            204.9201443105555,
                            220.69476736393938,
                            233.01825457124758,
                            241.42537594860903,
                            257.8370560989489,
                            276.78767285462266,
                            282.57921744810767,
                            292.2098255045404,
                            301.6917366173423,
                            316.88605369765514,
                            327.39226378798855,
                            338.9628620203142,
                            356.0673357706496,
                            365.654266456021,
                            377.67976214698086,
                            387.51585174367693,
                            397.16456699177576])

fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:blue'
ax1.set_xlabel('Generated Qubits from IBM Platform per execution', fontsize=22)
ax1.set_ylabel('Raw Key Rate (bps)', color=color, fontsize=22)
ax1.plot(qbit, raw_keyrate, color=color, marker='o', label='Sifted Key Rate (bps)', markersize=10)
ax1.tick_params(axis='y', labelcolor=color, labelsize=22)
ax1.tick_params(axis='x', labelsize=20)
ax1.set_ylim(0, 850)
ax1.set_xlim(0, 30)
ax1.set_xticks(np.arange(0, 30, 2))
ax1.set_yticks(np.arange(0, 850, 100))
ax1.grid(alpha=0.3)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Sifted Key Rate (bps)', color=color, fontsize=22)
ax2.plot(qbit, sifted_keyrate, color=color, marker='s', label='Runtime (s)', markersize=10)
ax2.tick_params(axis='y', labelcolor=color, labelsize=22)
ax2.set_ylim(0, 850)
ax2.set_yticks(np.arange(0, 850, 100))
ax2.grid(alpha=0.3)

# fig.suptitle('Generated Qubits from IBM Platform per Execution vs. Sifted Key Rate and Runtime')
fig.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.savefig('qlength_vs_raw_sifted_keyrate.png', format='png', bbox_inches="tight", dpi=300)

plt.show()
