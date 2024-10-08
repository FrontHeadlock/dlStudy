import numpy as np
import matplotlib.pylab as plt
def sigmoid(x):
    return 1 / (1+np.exp(-x))

x= np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))

t = np.array([1.0, 2.0, 3.0])
print(1.0 + t)
print(1.0 / t)

y = np.arange(-5.0, 5.0, 0.1)
y2 = sigmoid(y)
plt.plot(y, y2)
plt.ylim(-0.1, 1.1)
plt.show()


