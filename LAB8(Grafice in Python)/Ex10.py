import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3*np.pi, 360)

sinus = np.sin(x)
cosinus = np.cos(x)
tangenta = np.tan(x)
cotangenta =1/np.tan(x)

plt.plot(x, sinus)
plt.plot(x, cosinus)
#plt.plot(x, tangenta)
#plt.plot(x, cotangenta)

plt.grid(True)
plt.show()