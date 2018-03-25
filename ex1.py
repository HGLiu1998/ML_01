import numpy as np
data = np.genfromtxt("ex1data1.txt",delimiter=',')
m = len(data)
X = data[0:m-1,0]
Y = data[0:m-1,1]
