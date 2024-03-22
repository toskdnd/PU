import numpy as np
import pandas as pd



c = 1
a = np.pi #set border of f to 0
b = np.pi #set border of f to 0

def f(x,y): #made up function
    global c,a,b
    return np.sin(x)*np.sin(a-x)*np.sin(y)*np.sin(b-y)
def omega(n,m):
    global c,a,b
    np.pi*c*np.sqrt((n^2/a^2)+(m^2/b^2))
def

nmax = 10
mmax = nmax
for n in range(1,nmax+1):
    for m in range(1,mmax+1):
        print(n,m)

