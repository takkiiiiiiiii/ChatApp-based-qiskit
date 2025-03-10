import matplotlib.pyplot as plt
import numpy as np

# conefficient characterizing of parameter estimation = 0.75

intercept_resend_ratio = [0, 10, 20, 30, 40, 50]

# # Data for Channel noise = 0%
keyrate_0 = [
    138.01364741872138,
    97.49102622734407,
    70.12754594035027,
    31.468045502716784,
    0.6910822632147118,
    -28.81797185572949
]

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
    98.48764499039498,
    70.1361241890631,
    42.88712744901887,
    5.963348536401171,
    -17.38668050523497,
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
    63.56469212451335,
    41.561191488525694,
    26.290821014917075,
    -8.75398476028867,
    -100,
    -100
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
    28.086243396554377,
    14.964519619329131,
    -0.7679036914836851,
    -100,
    -100,
    -100
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
    12.601117708536618,
    0.29999159836470596,
    -22.300558065497057,
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
#     -5.240776095388059,
#     -100,
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
plt.ylim(0, 140)


plt.xticks(np.arange(0, 45, 10), fontsize=35)  # Increase font size for x-axis ticks
plt.yticks(np.arange(0, 141, 20), fontsize=35)  # Increase font size for y-axis ticks


# Adding labels and title
plt.xlabel('Intercept and Resend Ratio (%)', fontsize=35)
plt.ylabel('Final Key Rate (bps)', fontsize=35)
# plt.title('Final Key Rate vs Intercept and Resend Ratio at Different Channel Noise Levels')
plt.legend()
plt.grid(True)
plt.savefig('Final_KeyRate_vs_ITA_Ratio_Different_Channel_Noise_Levels2.png', format='png', bbox_inches="tight", dpi=300)

plt.legend(fontsize=25)


# Display the plot
plt.show()
