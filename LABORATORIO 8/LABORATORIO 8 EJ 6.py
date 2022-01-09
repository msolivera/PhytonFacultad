def contador_linea (archivo,cadena):

    archivo1=open(archivo)

    lineas=[]
    l=1

    for linea in archivo1:
        if cadena in linea:
            lineas.append(l)
            l=l+1

    archivo1.close()
    return lineas


print(contador_linea("C:\\Temp\\archivo1.txt","hola"))

