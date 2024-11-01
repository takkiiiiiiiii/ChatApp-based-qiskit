import matplotlib.pyplot as plt
import numpy as np


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
plt.plot(channel_noise_levels, qber_intercept_0, marker='o', label='IRA = 0%')
plt.plot(channel_noise_levels, qber_intercept_20, marker='s', label='IRA = 20%')
plt.plot(channel_noise_levels, qber_intercept_40, marker='h', label='IRA = 40%')
plt.plot(channel_noise_levels, qber_intercept_60, marker='x', label='IRA = 60%')
plt.plot(channel_noise_levels, qber_intercept_80, marker='p', label='IRA = 80%')
plt.plot(channel_noise_levels, qber_intercept_100, marker='D', label='IRA = 100%')

# Setting the plot limits and ticks
plt.xlim(0, 10)
plt.ylim(0, 32)
plt.xticks(channel_noise_levels)
plt.yticks(np.arange(0, 32, 5))

# Adding labels, title, and legend
plt.xlabel('Channel Noise (%)')
plt.ylabel('QBER (%)')
plt.title('QBER vs Channel Noise at Different Intercept and Resend Ratios')
plt.legend()
plt.grid(True)
plt.savefig('QBER_vs_Channel_Noise_Different_Intercept_and_Resend_Ratios.png', format='png', bbox_inches="tight", dpi=300)

# Display the plot
plt.show()
