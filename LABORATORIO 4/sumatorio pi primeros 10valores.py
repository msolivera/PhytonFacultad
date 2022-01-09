import math

def sumatoria (n):
    suma=0
    k=1
    while k<=n:
        suma =((1/16)**k)*((4/(8*k+1))-(2/(8*k+4))-(1/(8*k+5))+(1/(8*k+6)))
        print(suma)
        k = k+1

sumatoria(10)
print(math.pi)
