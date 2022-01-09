print ("BIENVENIDO AL PROGRAMA DE TRANSFORMACION DE CADENAS")
print ("")
print ("Ingrese a continuación la cadena de caracteres que desea modificar:")
cadena = input()
while len(cadena) == 0:
    print ("Debe ingresar al menos un caracter")
    cadena = input()
print ("MENU PRICIPAL")
print ("0- Modo Comando\n1 – Cambiar todas las letras de minúsculas a MAYÚSCULAS.\n2 – Cambiar de minúscula a Mayúscula la primera letra de todas las palabras.\n3 – Cambiar de MAYÚSCULAS a minúsculas todas las letras.\n4 – Quitar todos los espacios a la izquierda del texto.\n5 – Quitar todos los espacios a la derecha del texto.\n6 – Reemplazar todas las ocurrencias de un carácter o palabra por otro\n7 – Cifrado utilizando cifrado Cesar.\n8 – Descifrado utilizando cifrado Cesar.\n9 – Salir")

print ("Ingrese la opción deseada")

x = int(input())

while x != 9:

    if x == 0:
        print("BIENVENIDO AL MODO COMANDO\nIngrese los comandos deseados utilizando el separador ¨|¨")
        x = input("Ingrese la opción deseada")


    if ">" in str(x):
        m = x.split ("|")
        for i in range (len(m)-1):
            if ">" in str(m[i]):
                u=i
                m[i]=m[i].partition(">")
        indice = m[u].index (">")
        modificado = m[u][indice-1]
        modificador = m[u][indice+1]
        if modificado in cadena:
            cadena = cadena.split(modificado)
            cadena = modificador.join(cadena)
        else:
            print ("La palabra o caracter a sustituir no existe en la cadena")
        print (cadena)
        x = input("Ingrese la opción deseada")
            
        print (m)
        print (m[2])
        print (u)
        
    x=9
    
