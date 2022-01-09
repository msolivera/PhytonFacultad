def contador_de_cadenas (archivo,cadena):

    archivo1=open(archivo)
   
    c=0
    for linea in archivo1:
        print(linea)
        c+=linea.count(cadena)
       
    archivo1.close()
    return c
    

print(contador_de_cadenas("C:\\Temp\\archivo1.txt","hola"))


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


def indice (archivo,cadena):

    archivo1=open(archivo)

    indices=[]
    ind=1

    for lineas in archivo1:
        lineas=lineas.strip().split(" ")
        #print(lineas)
        for i in range (len(lineas)-1):
            if cadena in lineas:

               idx=lineas.index(cadena)

               indices.append(idx)
               ind+=1
             
    return indices
    


        
print(indice("C:\\Temp\\archivo1.txt","hola"))











    
