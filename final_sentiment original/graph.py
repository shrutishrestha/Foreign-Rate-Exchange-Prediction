import numpy as np
import matplotlib.pyplot as plt

x = [0,5,9,10,15,20,25,30]
y = [0,1]
plt.subplot(2,1,1)
plt.stem([1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0])
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.show()


a= [0,5,9,10,15,20,25,30]
b= [0,1]
plt.subplot(2,1,2)
plt.stem([1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0])
plt.xticks(np.arange(min(a), max(a)+1, 1.0))

plt.show()
