import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.loadtxt("TEMPvsPEA.dat")
data1 = np.loadtxt("TEMPvsPEA1.dat")

x = data[:,0]
y = data[:,1]

x1 = data1[:,0]
y1 = data1[:,1]

plt.figure()

plt.plot(x,y, linewidth=0.7, color="limegreen")
plt.plot(x1,y1, linewidth=0.7, color="limegreen")

plt.legend()

plt.xlabel("Temp")
plt.ylabel("U")
plt.xlim([500, 1900])
plt.ylim([-3.5,-3.9])
plt.savefig('Histerisis.png', dpi=1000)
plt.close()