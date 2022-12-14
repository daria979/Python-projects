import  matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
arr = np.array([1, 2, 3, 4, 5])
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

newarr = np.sum([arr1, arr2])

print(newarr)