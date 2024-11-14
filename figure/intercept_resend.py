import matplotlib.pyplot as plt
import numpy as np


# Data for Channel noise = 0%
intercept_resend_ratio = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
qber_0 = [0, 2.783203125, 5.400390625, 8.7890625, 10.966796875, 12.79296875, 
          14.6484375, 15.91796875, 19.04296875, 21.09375, 24.70703125]

# Data for Channel noise = 1%
qber_1 = [1.26953125, 3.61328125, 6.34765625, 9.66796875, 11.71875, 12.890625, 
          16.11328125, 17.138671875, 20.615234375, 23.076171875, 25.146484375]

# Data for Channel noise = 2%
qber_2 = [2.03125, 4.19921875, 6.943359375, 9.287109375, 11.748046875, 14.00390625, 
          16.630859375, 18.642578125, 22.001953125, 24.130859375, 26.103515625]

# Data for Channel noise = 3%
qber_3 = [3.0150494, 5.048828125, 8.076171875, 10.107421875, 11.904296875, 14.5703125, 17.119140625, 19.99023437, 22.607421875, 24.873046875, 27.109375]

# Data for Channel noise = 4%
qber_4 = [4.033203125, 5.888671875, 8.6328125, 10.615234375, 13.1640625, 15.380859375, 
          17.8125, 20.380859375, 22.32421875, 24.6484375, 27.197265625]

# Data for Channel noise = 5%
qber_5 = [5.048828125, 7.333984375, 9.375, 11.533203125, 14.033203125, 15.8984375, 
          18.017578125, 21.09375, 23.125, 25.498046875, 27.71484375]

qber_6 = [
    6.640625,
    7.8125,
    10.15625,
    11.650390625,
    13.908203125,
    16.337890625,
    18.935546875,
    21.97265625,
    23.6328125,
    25.43359375,
    27.783203125,
]

qber_8 = [
    7.6953125,
    10.78125,
    12.333984375,
    14.765625,
    15.810546875,
    19.7265625,
    20.76171875,
    22.63671875,
    24.53515625,
    25.78125,
    28.837890625,
]

qber_10 = [
    9.82421875,
    11.97265625,
    14.228515625,
    14.61875,
    16.884765625,
    20.8984375,
    22.01171875,
    23.7890625,
    25.400390625,
    27.255859375,
    30.46875,
]

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
