import numpy as np
import matplotlib.pyplot as plt
from decimal import *

def hypothesis():
    return np.dot(X,theta)
def Cost_func():
    Cost = hypothesis()-Y
    sum = 0.0
    for i in range(0,m):
        sum += np.square(Cost[i][0])
    return sum
data = np.genfromtxt("ex1data1.txt",delimiter=',')
m = len(data)
X = np.array(data[0:m,0]).reshape(m,1)
Y = np.array(data[0:m,1]).reshape(m,1)
#print(X)
#print(type(X))
#print((X is data[0:m-1,0]))
#plt.style.use('ggplot')
#plt.plot(X,Y,'b.')
#plt.show()
X = np.hstack((np.ones((m,1)), X))
theta = np.array([[-1],[-2]],dtype = np.float)

#print(getcontext()) 浮點數精度查詢

print(Cost_func())