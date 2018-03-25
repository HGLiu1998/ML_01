import numpy as np
import matplotlib.pyplot as plt

def hypothesis(x):
    return theta[0][0] + theta[1][0] * x



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
print(theta)
print(hypothesis(2))

