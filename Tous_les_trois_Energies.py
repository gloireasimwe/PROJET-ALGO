import numpy as np
import matplotlib.pyplot as plt
from math import*

x = [0.01]
v,t = [0] , [0]
h = 1e-3


for i in range(0,10000):
    x.append(x[i]+h*v[i])
    v.append((1-h)*v[i]-100*h*x[i-1]+h*cos(10*i*h))
    t.append(i*h)

a = np.array(x)
c = np.array(v)
temp = np.array(t)

ep = 10*9.81*a
ec = 0.5*10*(c**2)
em= ec + ep


plt.plot(temp,ep, color = 'blue' )

plt.plot(temp,ec, color = 'red' )

plt.plot(temp,em, color = 'green')
plt.show()