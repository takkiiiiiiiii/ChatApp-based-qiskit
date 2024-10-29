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




# Plotting the data
plt.figure(figsize=(8, 5))
plt.plot(intercept_resend_ratio, qber_0, marker='o', label='Channel noise = 0%')
plt.plot(intercept_resend_ratio, qber_1, marker='s', label='Channel noise = 1%')
plt.plot(intercept_resend_ratio, qber_2, marker='h', label='Channel noise = 2%')
plt.plot(intercept_resend_ratio, qber_3, marker='x', label='Channel noise = 3%')
plt.plot(intercept_resend_ratio, qber_4, marker='p', label='Channel noise = 4%')
plt.plot(intercept_resend_ratio, qber_5, marker='D', label='Channel noise = 5%')


plt.xlim(0, 100)
plt.ylim(0, 27)


plt.yticks(np.arange(0, 32, 5))
plt.xticks(np.arange(0, 101, 10))


# Adding labels and title
plt.xlabel('Intercept and Resend Ratio (%)')
plt.ylabel('QBER (%)')
plt.title('QBER vs Intercept and Resend Ratio at Different Channel Noise Levels')
plt.legend()
plt.grid(True)
plt.savefig('QBER_vs_ITA_Ratio_Different_Channel_Noise_Levels.png', format='png', bbox_inches="tight", dpi=300)

# Display the plot
plt.show()
