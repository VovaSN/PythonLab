import math

def FindP(y,f): 
    x1 = 1 + (2*y /(y-1)) - f**2
    x2 = 2*y / (y-1) - 1
    x3 = math.sqrt(x1**2 - 4*f**2*x2)
    x4 = 2*f**2*x2
    x5 = 1- ((x1 - x3) / x4)
    P = x5**(y/(y-1))
   

    return P

print(FindP(1.4,0.5))