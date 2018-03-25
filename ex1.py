import numpy as np
import matplotlib.pyplot as plt
from decimal import *


np.set_printoptions(precision = 4)

data = np.genfromtxt("ex1data1.txt",delimiter=',')
m = len(data)
X = np.array(data[0:m,0]).reshape(m,1)
Y = np.array(data[0:m,1]).reshape(m,1)
#plt.style.use('ggplot')
#plt.plot(X,Y,'b.')
#plt.show()
X = np.hstack((np.ones((m,1)), X))
theta = np.array([[-1],[-2]],dtype = np.float)

#print(getcontext()) 浮點數精度查詢
#define hypothesis and Cost function
def hypothesis():
    return np.dot(X,theta)
def Cost_func():
    Cost = hypothesis()-Y
    sum = 0.0
    for i in range(0,m):
        print(np.around(Cost[i][0], decimals = 4))
        sum += np.square(Cost[i][0])
    return np.around(sum,decimals = 4)
print(Cost_func())