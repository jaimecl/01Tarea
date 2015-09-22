import numpy as np
import matplotlib.pyplot as plt


a, b = np.loadtxt("sun_AM0.dat.dat", unpack="True")

plt.plot(np.log10(a),np.log10(b))
plt.show()
