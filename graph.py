import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt(r"descent_data.txt")
h = data[:, 0]
v_r = data[:, 1]
v_r_target = data[:, 2]

plt.plot(h, v_r, label='Actual descent rate')
plt.plot(h, v_r_target, label='Target descent rate')
plt.xlabel("Altitude (m)")
plt.ylabel("Descent rate (m/s)")
plt.gca().invert_xaxis()  # Show higher altitudes on left
plt.legend()
plt.grid()
plt.show()