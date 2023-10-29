from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import math
import statsmodels.api as sm
import pylab as py

f=open('C:/Users/Fareed/Downloads/samples.txt','r')
data = f.readlines()
data = [i.replace('\n','') for i in data]
for i in range(0, len(data)):
    data[i] = float(data[i])



#الف
avrage = sum(data) / len(data)
print('avrage equal to: ')
print(avrage)
variance = 0
for i in data:
    variance += (i - avrage)**2 
variance = variance / len(data)
print('variance equal to: ')
print(variance)
print('________________')
#ب
plt.subplot(1, 2, 1)
plt.hist(x=data, bins='auto')
plt.title('histogram')

#ج
data.sort()
d = [0 for i in range(0, 1000)]
counter = 1
for i in range(0,1000):
    d[i]=norm.cdf(norm.ppf((counter - 0.5)/1000))
    counter = counter + 1
plt.subplot(1, 2, 2)
plt.scatter( data,d)
plt.title('Q-Q')
plt.show()
#د
alpha = 1.36/math.sqrt(1000)
m1 = max(data)
m2 = min(data)
for i in data:
    i = (i - m2)/(m1 - m2)
D_plus = (1/1000) - data[0]
D_negative = data[0]
for i  in range(1,1000):
    temp_D_plus = ((i+1)/1000) - data[i]
    temp_D_negative = data[i] - (i/1000)
    if temp_D_plus > D_plus:
        D_plus = temp_D_plus
    if temp_D_negative > D_negative : 
        D_negative = temp_D_negative
    
D = 0
if D_negative > D_plus : 
    D = D_negative
else :
    D = D_plus
if(D < alpha):
    print('accept:))')
else:
    print('rejcet:((')


