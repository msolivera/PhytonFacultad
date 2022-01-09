def buscar(cadena,subcadena):
    if subcadena in cadena:
        for i in range (len(cadena)-len(subcadena)+1):
            if cadena[i:i+len(subcadena)]==subcadena:
                return i
    else:
        return -1
        
print(buscar("hoy es miercoles","col"))



#len(cadena)-len(subcadena)
#cadena[i:i+len(subcadena)]==subcadena: i arranca en 0 y va a ir comparando
#hoy==col? y asi susesivamente.
#return -1 se usa para decir si recorre toda la cadena u no encuentra "col"
