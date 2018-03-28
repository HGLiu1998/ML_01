import numpy as np 
import matplotlib as plt
data = np.genfromtxt("ex1data2.txt",delimiter = ',')
m = len(data)
x = np.array(data[0:m,0:2])
Y = np.array(data[0:m,2]).reshape(m,1)
print(x)
print(Y)
