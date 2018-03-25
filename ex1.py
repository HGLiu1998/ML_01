import numpy as np
import matplotlib.pyplot as plt

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
    sum = np.sum(np.square(Cost))/(2*m)
    return np.around(sum,decimals = 8)
print(hypothesis())
print(Cost_func())