def sumatoria (n):
    suma=0
    termino=1
    while termino<=n:
        suma+= termino**2
        termino+= 1
        return suma

print (sumatoria(2))
