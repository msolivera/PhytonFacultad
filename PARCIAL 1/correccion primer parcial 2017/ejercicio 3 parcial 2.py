def ejercicio(lineas,columna,espacio,nombre):
    for i in range(lineas):
        print((nombre+(' '*espacio))*columna)
        i=i+1
ejercicio(5,5,4,"x")
