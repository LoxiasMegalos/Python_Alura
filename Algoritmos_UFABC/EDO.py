#from matplotlib import pyplot as plt
#from scipy.integrate import odeint
#import numpy as np

#def f(u,x):
#    return (u[1],-2*u[1]-2*u[0]+np.cos(2*x))
#y0 = [1,0]
#xs = np.linspace(1,10,200)
#us = odeint(f,y0,xs)
#ys = us[:,0]
#plt.plot(xs,ys,'-')
#plt.plot(xs,ys,'r*')
#plt.xlabel('x values')
#plt.ylabel('y values')
#plt.title('(D**2+2D+2)y = cos(2*x)')
#plt.show()

import sympy as sp

sp.init_printing()

y = sp.Function('y')
x = sp.symbols('x')

exact = sp.dsolve((x*y(x).diff(x,2)) -(3*y(x).diff(x,1)) +((4/x)*y(x)) - 2*x + 1, ics={y(1):0, y(2):0})