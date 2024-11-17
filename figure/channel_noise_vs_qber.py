import matplotlib.pyplot as plt
import numpy as np


qber_0 = [
    0,
    1.7973917748917732,
    3.4140945165945165,
    7.175812798312818,
    8.486754356754382,
    12.971031746031771,
    14.56709235209237,
    17.344290986790995,
    20.337601842601806,
    21.048529248529242,
    25.18423021423021]

# Data for Channel noise = 1%
# qber_1 = []

# Data for Channel noise = 2%
qber_2 = [2.0793795093795078,
        3.551919191919191,
        5.334590964590978,
        8.87770535020537,
        10.210599955599985,
        14.140735930735957,
        15.383792596292606,
        17.56914862914863,
        20.166054501054475,
        22.507860472860425,
        26.47619047619046]

# Data for Channel noise = 3%
# qber_3 = []

# Data for Channel noise = 4%
qber_4 = [4.114765512265522,
5.835752780197241,
7.094224386724409,
10.521241813741844,
12.719246864246896,
15.548935786435791,
17.689747474747477,
18.61751914751914,
22.04626678876677,
24.814696969696932,
26.502539682539645]

# Data for Channel noise = 5%
# qber_5 = []

qber_6 = [5.961298701298715,
7.1903571428571595,
9.00855339105342,
11.908850038850083,
14.068243145743159,
16.30529442779442,
19.239832667332674,
20.126277056277036,
23.516985236985207,
25.298953823953784,
27.493766233766245,]

qber_8 = [7.904286546786567,
9.246509046509074,
10.874034207367576,
13.900764790764825,
15.936272061272087,
18.070965978465996,
20.120453157953147,
21.880573593073592,
24.935850213627987,
26.492829115329126,
28.431505994006002]

qber_10 = [
    10.362176473287617,
    11.503740981241005,
    13.212064324564357,
    15.616693861693875,
    16.936471861471862,
    19.429650904650906,
    21.137222222222192,
    22.13251852140738,
    26.07321428571429,
    27.10765123765122,
    30.064628427128397]

# Data arrays for Channel Noise levels and respective QBER values at specific Intercept and Resend Ratios
channel_noise_levels = [0, 2, 4, 6, 8, 10]

qber_intercept_0 = [qber_0[0], qber_2[0], qber_4[0], qber_6[0], qber_8[0], qber_10[0]]
qber_intercept_20 = [qber_0[2], qber_2[2], qber_4[2], qber_6[2], qber_8[2], qber_10[2]]
qber_intercept_40 = [qber_0[4], qber_2[4],  qber_4[4], qber_6[4], qber_8[4], qber_10[4]]
qber_intercept_60 = [qber_0[6], qber_2[6], qber_4[6], qber_6[6], qber_8[6], qber_10[6]]
qber_intercept_80 = [qber_0[8], qber_2[8], qber_4[8], qber_6[8], qber_8[8], qber_10[8]]
qber_intercept_100 = [qber_0[10], qber_2[10], qber_4[10], qber_6[10], qber_8[10], qber_10[10]]

# Plotting the data for each Intercept and Resend Ratio
plt.figure(figsize=(10, 6))
plt.plot(channel_noise_levels, qber_intercept_0, marker='o', label='IRA = 0%', markersize=20)
plt.plot(channel_noise_levels, qber_intercept_20, marker='s', label='IRA = 20%', markersize=20)
plt.plot(channel_noise_levels, qber_intercept_40, marker='h', label='IRA = 40%', markersize=20)
plt.plot(channel_noise_levels, qber_intercept_60, marker='x', label='IRA = 60%', markersize=20)
plt.plot(channel_noise_levels, qber_intercept_80, marker='p', label='IRA = 80%', markersize=20)
plt.plot(channel_noise_levels, qber_intercept_100, marker='D', label='IRA = 100%', markersize=20)

# Setting the plot limits and ticks
plt.xlim(0, 10)
plt.ylim(0, 35)
plt.xticks(channel_noise_levels, fontsize=35)
plt.yticks(np.arange(0, 35, 5), fontsize=35)

# Adding labels, title, and legend
plt.xlabel('Channel Noise (%)', fontsize=35)
plt.ylabel('QBER (%)', fontsize=35)
# plt.title('QBER vs Channel Noise at Different Intercept and Resend Ratios')
plt.grid(True)
plt.savefig('QBER_vs_Channel_Noise_Different_Intercept_and_Resend_Ratios.png', format='png', bbox_inches="tight", dpi=300)


plt.legend(fontsize=25)
# Display the plot
plt.show()
