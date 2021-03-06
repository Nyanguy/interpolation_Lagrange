import numpy as np
import matplotlib.pyplot as mp
from math import sin,cos,tan,pi

def interpolation(x,n,a,b,vec_x):
    """
    :param x: coordinate
    :param n: amount of connections
    :param a: start point
    :param b: end point
    :param vec_x: array of initial x coordinates
    :return: array of dots for interpolated function
    """
    node = [cos((i/float(n))*pi)*(b-a)/2 for i in range(0,n)] #Chebish
    sums=0
    k=1.
    for i in range(0,n):
        k=1.
        for j in range(n-1,n-i,-1):
            k*=(a-node[j])
        sums+=vec_x[i]*k
    return sums
x = [i for i in np.arange(-1.5,1.5,0.1)]
y = [tan(i) for i in x]
yi = [interpolation(i,5,-1.5,1.5,x) for i in x]
mp.plot(x,y,color="r")
mp.plot(x,yi,color="b")
mp.grid(True)
mp.show()

