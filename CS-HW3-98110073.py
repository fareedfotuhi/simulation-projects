from random import randint
import numpy as np
import matplotlib.pyplot as plt


n = int(input())
matrix = []
first = list(map(int,input().split()))
for i in range(n):
    temp = list(map(float,input().split()))
    matrix.append(temp)

    
x = randint(100,10000)
h = first
result = []
for i in range(x):
    m3 = np.dot(h,matrix)
    h = m3
    result.append(m3)


t = []
for i in range(1,x + 1):
    t.append(i)

for i in range(n):
    plt.plot(t,result[:][i])

    
plt.show()