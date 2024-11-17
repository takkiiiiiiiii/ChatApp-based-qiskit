import matplotlib.pyplot as plt
import numpy as np


# Data for Channel noise = 0%
intercept_resend_ratio = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
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

# Plotting the data
plt.figure(figsize=(8, 5))
plt.plot(intercept_resend_ratio, qber_0, marker='o', label='Channel noise = 0%', markersize=20)
plt.plot(intercept_resend_ratio, qber_2, marker='s', label='Channel noise = 2%' ,markersize=20)
plt.plot(intercept_resend_ratio, qber_4, marker='h', label='Channel noise = 4%', markersize=20)
plt.plot(intercept_resend_ratio, qber_6, marker='x', label='Channel noise = 6%', markersize=20)
plt.plot(intercept_resend_ratio, qber_8, marker='p', label='Channel noise = 8%', markersize=20)
plt.plot(intercept_resend_ratio, qber_10, marker='D', label='Channel noise = 10%', markersize=20)

plt.xlim(0, 100)
plt.ylim(0, 32)


plt.yticks(np.arange(0, 32, 5), fontsize=35)
plt.xticks(np.arange(0, 101, 10), fontsize=35)


# Adding labels and title
plt.xlabel('Intercept and Resend Ratio (%)', fontsize=35)
plt.ylabel('QBER (%)', fontsize=35)
# plt.title('QBER vs Intercept and Resend Ratio at Different Channel Noise Levels')
plt.legend()
plt.grid(True)
plt.savefig('QBER_vs_ITA_Ratio_Different_Channel_Noise_Levels.png', format='png', bbox_inches="tight", dpi=300)


plt.legend(fontsize=25)

# Display the plot
plt.show()
