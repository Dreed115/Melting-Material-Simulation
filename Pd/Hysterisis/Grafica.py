import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.loadtxt("TEMPvsPEA_Enfria.dat")
data1 = np.loadtxt("TEMPvsPEA_Calienta.dat")
data2 = np.loadtxt("TEMPvsPEA.dat")

x = data[:,0]
y = data[:,1]

x1 = data1[:,0]
y1 = data1[:,1]

x2 = data2[:,0]
y2 = data2[:,1]

plt.figure()

plt.plot(x,y, linewidth=0.7, color="limegreen")
plt.plot(x1,y1, linewidth=0.7, color="limegreen")
plt.plot(x2,y2, linewidth=0.7, color="limegreen")

plt.legend()

plt.xlabel("Temp")
plt.ylabel("U")
plt.xlim([800, 2050])
plt.ylim([-3.40,-3.95])
plt.savefig('Histerisis.png', dpi=1000)
plt.close()