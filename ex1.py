import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("ex1data1.txt",delimiter=',')
m = len(data)
X = np.array(data[0:m-1,0])
Y = np.array(data[0:m-1,1])
#print(type(X))
#print((X is data[0:m-1,0]))
plt.plot(X,Y,'ro')
plt.show()

