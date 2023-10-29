from numpy import log as ln
import math
import random

landa = [0 for i in range(0, 3)]
landa[0] = 30
landa[1] = 50
landa[3] = 20
landa_star= max(landa)
t = 0
i = 1
T = []
while 1==1:
    R = random.uniform()
    E = -1*landa_star*ln(R)
    t = t + E
    R = random.uniform()
    landa_temp = 0
    if t >= 9 and t <= 12:
        landa_temp = landa[0]
    elif t>12 and t<14:
        landa_temp = landa[1]
    elif t >= 14 and t <= 17:
        landa_temp = landa[2]
    elif t > 17:
        break
    
    x =landa_temp/ landa_star
    if x >= R:
        T.append(t)
        i = i + 1
    

print(T)
print('\n')
print(i)