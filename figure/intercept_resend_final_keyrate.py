import matplotlib.pyplot as plt
import numpy as np


intercept_resend_ratio = [0, 10, 20, 30, 40, 50]

# # Data for Channel noise = 0%
# keyrate_0 = [
#     0.4970905368399544,
#     0.38878548978641625,
#     0.23462850350558143,
#     0.0972451385226684,
#     -0.008122235088976916,
#     -0.0739168284062181
# ]
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
# keyrate_2 = [
#     0.34688802093838433,
#     0.2528187245757023,
#     0.14332935012052278,
#     0.04339751139744282,
#     -0.04684597921879155,
#     -0.12577826518331722,
# ]

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
# keyrate_4 = [
#     0.23672713889465177,
#     0.1779948666282466,
#     0.05958104606200918,
#     -0.009066046190307998,
#     -100,
#     -100,
# ]

# # Data for Channel noise = 5%
# keyrate_5 = [
#     0.17854664278105895,
#     0.12014674471086695,
#     0.030968289587492426,
#     -0.06622548548820373,
#     -100,
#     -100,
# ]

# keyrate_6 = [
#     0.13644054071419148,
#     0.08747306246569848,
#     -0.006473900425140899,
#     -0.08101399655111927,
#     -100,
#     -100,
# ]


# keyrate_7 = [
#     0.09974184418859175,
#     0.04517169082679395,
#     -0.027726021208254403,
#     -0.1209675146933971,
#     -100,
#     -100,
# ]

# keyrate_8 = [
#     0.04743629181225153,
#     0.01926258733302285,
#     -0.08184446359356777,
#     -100,
#     -100,
#     -100
# ]

# keyrate_9 = [
#     0.018840671790663212,
#     -0.09167206847175288,
#     -100,
#     -100,
#     -100,
#     -100
# ]

# keyrate_10 = [
#     -0.01938645420814274,
#     -0.05762118091531464,
#     -100,
#     -100,
#     -100,
#     -100
# ]


keyrate_0 = [159.07, 124.41, 75.08, 31.12, -2.60, -23.65]
keyrate_1 = [126.82, 100.47, 63.11, 25.06, -8.57, -32.51]
keyrate_2 = [111.00, 80.90, 45.87, 13.89, -14.99, -40.25]
keyrate_3 = [91.96, 65.61, 26.13, 4.38, -22.18, -32000]
keyrate_4 = [75.75, 56.96, 19.07, -2.90, -32000, -32000]
keyrate_5 = [57.13, 38.45, 9.91, -21.19, -32000, -32000]
keyrate_6 = [43.66, 27.99, -2.07, -25.92, -32000, -32000]
keyrate_7 = [31.92, 14.45, -8.87, -38.71, -32000, -32000]
keyrate_8 = [15.18, 6.16, -26.19, -32000, -32000, -32000]
keyrate_9 = [6.03, -29.34, -32000, -32000, -32000, -32000]
keyrate_10 = [-6.20, -18.44, -32000, -32000, -32000, -32000]
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


plt.xlim(0, 55)
plt.ylim(0, 161)


plt.xticks(np.arange(0, 55, 10), fontsize=35
           )  # Increase font size for x-axis ticks
plt.yticks(np.arange(0, 161, 20), fontsize=35)  # Increase font size for y-axis ticks



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
