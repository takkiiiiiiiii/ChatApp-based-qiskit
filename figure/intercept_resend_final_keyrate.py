import matplotlib.pyplot as plt
import numpy as np

# conefficient characterizing of parameter estimation = 0.9

intercept_resend_ratio = [0, 10, 20, 30, 40, 50]

# # Data for Channel noise = 0%
keyrate_0 = [
    165.61637690246565,
    116.9823049705645,
    83.01615031828119,
    47.65612203640658,
    1.923709429671463,
    -36.61686573711773]

# # Data for Channel noise = 1%
# keyrate_1 = [
#     0.3963073909521176,
#     0.31395620490646264,
#     0.19722535409885122,
#     0.0783264590465125,
#     -0.026782815858066022,
#     -0.10159030127835726,
# ]

# # Data for Channel noise = 2%
keyrate_2 = [
    117.75890763290957,
    82.55865124493084,
    54.31759749138055,
    12.495575332663096,
    -18.810675733079467,
    -100
]

# # Data for Channel noise = 3%
# keyrate_3 = [
#     0.2873890387223058,
#     0.20504194507184642,
#     0.08166770145411653,
#     0.013699891154148065,
#     -0.06930618043609085,
#     -100
# ]

# # Data for Channel noise = 4%
keyrate_4 = [
    80.0731899431464,
    58.26673108381603,
    23.18539859462765,
    -13.079897804761355,
    -100,
    -100,
]

# # Data for Channel noise = 5%
# keyrate_5 = [
#     0.17854664278105895,
#     0.12014674471086695,
#     0.030968289587492426,
#     -0.06622548548820373,
#     -100,
#     -100,
# ]

keyrate_6 = [
    47.0939134991444,
    23.7590422018253,
    5.547264146512772,
    -28.40068313122474,
    -100,
    -100,
]


# keyrate_7 = [
#     0.09974184418859175,
#     0.04517169082679395,
#     -0.027726021208254403,
#     -0.1209675146933971,
#     -100,
#     -100,
# ]

keyrate_8 = [
    11.995965851890528,
    -0.45568591200458125,
    -6.342538830650283,
    -100,
    -100,
    -100
]

# keyrate_9 = [
#     0.018840671790663212,
#     -0.09167206847175288,
#     -100,
#     -100,
#     -100,
#     -100
# ]

# keyrate_10 = [
#     -2.64118188125766,
#     -4.162515006979562,
#     -100,
#     -100,
#     -100,
#     -100
# ]


# keyrate_0 = [159.07, 124.41, 75.08, 31.12, -2.60, -23.65]
# keyrate_1 = [126.82, 100.47, 63.11, 25.06, -8.57, -32.51]
# keyrate_2 = [111.00, 80.90, 45.87, 13.89, -14.99, -40.25]
# keyrate_3 = [91.96, 65.61, 26.13, 4.38, -22.18, -32000]
# keyrate_4 = [75.75, 56.96, 19.07, -2.90, -32000, -32000]
# keyrate_5 = [57.13, 38.45, 9.91, -21.19, -32000, -32000]
# keyrate_6 = [43.66, 27.99, -2.07, -25.92, -32000, -32000]
# keyrate_7 = [31.92, 14.45, -8.87, -38.71, -32000, -32000]
# keyrate_8 = [15.18, 6.16, -26.19, -32000, -32000, -32000]
# keyrate_9 = [6.03, -29.34, -32000, -32000, -32000, -32000]
# keyrate_10 = [-6.20, -18.44, -32000, -32000, -32000, -32000]
# Plotting the data
plt.figure(figsize=(8, 5))
plt.plot(intercept_resend_ratio, keyrate_0, marker='o', label='Channel noise = 0%', markersize=20)
# plt.plot(intercept_resend_ratio, keyrate_1, marker='*', label='Channel noise = 1%')
plt.plot(intercept_resend_ratio, keyrate_2, marker='s', label='Channel noise = 2%', markersize=20)
# plt.plot(intercept_resend_ratio, keyrate_3, marker='v', label='Channel noise = 3%')
plt.plot(intercept_resend_ratio, keyrate_4, marker='h', label='Channel noise = 4%', markersize=20)
# plt.plot(intercept_resend_ratio, keyrate_5, marker='^', label='Channel noise = 5%')
plt.plot(intercept_resend_ratio, keyrate_6, marker='x', label='Channel noise = 6%', markersize=20)
# plt.plot(intercept_resend_ratio, keyrate_7, marker='+', label='Channel noise = 7%')
plt.plot(intercept_resend_ratio, keyrate_8, marker='p', label='Channel noise = 8%', markersize=20)
# plt.plot(intercept_resend_ratio, keyrate_9, marker='H', label='Channel noise = 9%')
# plt.plot(intercept_resend_ratio, keyrate_10, marker='D', label='Channel noise = 10%', markersize=20)


plt.xlim(0, 45)
plt.ylim(0, 170)


plt.xticks(np.arange(0, 45, 10), fontsize=35)  # Increase font size for x-axis ticks
plt.yticks(np.arange(0, 171, 20), fontsize=35)  # Increase font size for y-axis ticks


# Adding labels and title
plt.xlabel('Intercept and Resend Ratio (%)', fontsize=35)
plt.ylabel('Final Key Rate (bps)', fontsize=35)
# plt.title('Final Key Rate vs Intercept and Resend Ratio at Different Channel Noise Levels')
plt.legend()
plt.grid(True)
plt.savefig('Final_KeyRate_vs_ITA_Ratio_Different_Channel_Noise_Levels.png', format='png', bbox_inches="tight", dpi=300)

plt.legend(fontsize=25)


# Display the plot
plt.show()
