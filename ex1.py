import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("ex1data1.txt",delimiter=',')
m = len(data)
x = np.array(data[0:m,0]).reshape(m,1)
Y = np.array(data[0:m,1]).reshape(m,1)

X = np.hstack((np.ones((m,1)), x))
theta = np.array([[-1],[-2]])

#print(getcontext()) 浮點數精度查詢
#define hypothesis and Cost function
def hypothesis():
    return np.dot(X,theta)
def Cost_func():
    Cost = hypothesis()-Y  
    sum = np.sum(np.square(Cost))/(2*m)
    return sum

print("beforeGD:",Cost_func())

iteration = 2500
learningrate = 0.01
def Gradient_descent():
    global theta
    for i in range(iteration):
        loss = hypothesis()-Y
        G = (X.T).dot(loss)/m #(2*97)*(97*1) 
        theta = theta - learningrate * G
    return theta
Gradient_descent()
print (theta)
print("afterGD:",Cost_func())
#plt.style.use('ggplot')
#plt.plot(x,Y,'b.')
#plt.plot(x,hypothesis())
#plt.show()