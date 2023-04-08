

from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy as np
import re
import math


""" les graphiques"""
# F(t) = 20cos(5t)


def f(u,x):
    return (u[1],-2*u[1]-400*u[0]+20*np.cos(5*x))

x0 = [0.01,0]

xs = np.linspace(1,10,400)
us = odeint(f,x0,xs)
ys =us[:,0]




plt.plot(xs,ys,'-')
plt.plot(xs,ys,'r*')
plt.xlabel("  x")
plt.ylabel(" y")
plt.plot("avec F(t) = Fo x Cos(wt) ")
plt.show()




#F(t)=F0cos(wt)
