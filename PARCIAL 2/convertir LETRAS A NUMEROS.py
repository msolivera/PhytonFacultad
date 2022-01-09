#para simplificar la condicion de vocales a e i o u, usamos """in"""
#if cadena[i] in "aeiou"
#para sustituir vocales por letras nos va a saltar un error debido a que python no puede sumar
#letras y numeros, sin embargo podemos usar una conversion que es ""STR""
#CONVERTIRA:LA REPRESENTACION DE LAS NUMEROS Y LO PODEMOS SUMAR A LOS CARACTERES

def codificar(contraseña):
    resultado=""
    contador=1
    for i in range (len(contraseña)):
        if contraseña [i] in "aeiouAEIOU":
            resultado+=str(contador)
            contador=contador+1
        else:
            resultado+=contraseña[i]
    return resultado
                
            
print(codificar("programacion"))        
