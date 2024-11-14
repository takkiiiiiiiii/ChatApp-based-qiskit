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



runtime = np.array([0.02712997055053711,
                    0.028251508474349974,
                    0.029165334701538086,
                    0.02939863395690918,
                    0.02908745360374451,
                    0.030076908111572265,
                    0.03076225996017456,
                    0.030799660682678223,
                    0.03159714508056641,
                    0.03191257405281067,
                    0.03230700922012329,
                    0.03203750014305115,
                    0.032225284337997435,
                    0.032888741254806515,
                    0.03349256300926209,
                    0.0340840208530426,
                    0.03428083062171936,
                    0.03377020215988159,
                    0.0348346312046051,
                    0.03511367154121399,
                    0.03624898648262024,
                    0.03617152690887451,
                    0.03595671463012695,
                    0.0365876567363739,
                    0.036102259635925296,
                    0.03690258097648621,
                    0.037262590169906615,
                    0.03715802240371704,
                    0.037488790035247806])

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
ax1.set_yticks(np.arange(0, 850, 50))
ax1.grid(alpha=0.3)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Execution time(s)', color=color, fontsize=22)
ax2.plot(qbit, runtime, color=color, marker='s', label='Runtime (s)', markersize=10)
ax2.tick_params(axis='y', labelcolor=color, labelsize=22)
ax2.set_ylim(0, 0.11)
ax2.set_yticks(np.arange(0, 0.11, 0.05))
ax2.grid(alpha=0.3)

# fig.suptitle('Generated Qubits from IBM Platform per Execution vs. Sifted Key Rate and Runtime')
fig.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.savefig('qlength_vs_raw_sifted_keyrate.png', format='png', bbox_inches="tight", dpi=300)

plt.show()
