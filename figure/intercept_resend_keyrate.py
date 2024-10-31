import matplotlib.pyplot as plt
import numpy as np


intercept_resend_ratio = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Data for Channel noise = 0%
keyrate_0 = [
    974.4632419383504,
    944.8445864281342,
    941.141777385607,
    905.2558219585131,
    884.458987427202,
    854.832133863112,
    809.2349631086635,
    795.1535600937227,
    761.7649969294564,
    743.141267492521,
    702.3238945447977
]
# Data for Channel noise = 1%
keyrate_1 = [
    960.162786479112,
    931.762214445465,
    920.0097762214115,
    903.4287799759301,
    864.1738784002088,
    823.4556966023454,
    800.4453995985868,
    773.1984477360796,
    768.4237740434372,
    735.187750761462,
    689.228246947672
]

# Data for Channel noise = 2%
keyrate_2 = [
    936.7183582179626,
    918.7746419898376,
    906.6233147057128,
    881.9343210180821,
    860.4739560316691,
    845.4502899022198,
    792.0340091102544,
    779.1298974764995,
    760.6472255185442,
    726.5140734301059,
    692.8709831424055
]

# Data for Channel noise = 3%
keyrate_3 = [
    931.6396218204063,
    904.2499655145027,
    891.1623119320699,
    871.7195201175498,
    850.9082475126145,
    803.5185177622856,
    782.5917984537831,
    765.2304871025601,
    737.7298509477706,
    717.7981653746564,
    684.1709948110506
]

# Data for Channel noise = 4%
keyrate_4 = [
    919.3033351810122,
    902.7295605360066,
    886.1351806507962,
    865.1017760914172,
    844.4555111724212,
    788.8965952398049,
    775.4174522256349,
    753.4367010353488,
    736.6795058666877,
    712.1957123024565,
    672.0406036961966
]

# Data for Channel noise = 5%
keyrate_5 = [
    913.5550128590864,
    899.920805052182,
    834.4074398087034,
    821.5932433496025,
    819.599602851847,
    792.5128647253082,
    750.1199985681202,
    740.1454647558453,
    723.8580097655304,
    709.8867062731027,
    669.9585736916241
]


# Plotting the data
plt.figure(figsize=(8, 5))
plt.plot(intercept_resend_ratio, keyrate_0, marker='o', label='Channel noise = 0%')
plt.plot(intercept_resend_ratio, keyrate_1, marker='s', label='Channel noise = 1%')
plt.plot(intercept_resend_ratio, keyrate_2, marker='h', label='Channel noise = 2%')
plt.plot(intercept_resend_ratio, keyrate_3, marker='x', label='Channel noise = 3%')
plt.plot(intercept_resend_ratio, keyrate_4, marker='p', label='Channel noise = 4%')
plt.plot(intercept_resend_ratio, keyrate_5, marker='D', label='Channel noise = 5%')


plt.xlim(0, 100)
plt.ylim(650, 1000)


plt.yticks(np.arange(650, 1000, 50))
plt.xticks(np.arange(0, 101, 10))


# Adding labels and title
plt.xlabel('Intercept and Resend Ratio (%)')
plt.ylabel('Sifted Key Rate (bps)')
plt.title('Sifted Key Rate vs Intercept and Resend Ratio at Different Channel Noise Levels')
plt.legend()
plt.grid(True)
plt.savefig('SiftedKey_Rate_vs_ITA_Ratio_Different_Channel_Noise_Levels.png', format='png', bbox_inches="tight", dpi=300)

# Display the plot
plt.show()
