print ("BIENVENIDO AL PROGRAMA DE TRANSFORMACION DE CADENAS")
print ("")
print ("Ingrese a continuación la cadena de caracteres que desea modificar:")
cadena = input()
while len(cadena) == 0:
    print ("Debe ingresar al menos un caracter")
    cadena = input()

print ("")
print ("MENU PRICIPAL")
print ("")
print ("0- Modo Comando\n1 – Cambiar todas las letras de minúsculas a MAYÚSCULAS.\n2 – Cambiar de minúscula a Mayúscula la primera letra de todas las palabras.\n3 – Cambiar de MAYÚSCULAS a minúsculas todas las letras.\n4 – Quitar todos los espacios a la izquierda del texto.\n5 – Quitar todos los espacios a la derecha del texto.\n6 – Reemplazar todas las ocurrencias de un carácter o palabra por otro\n7 – Cifrado utilizando cifrado Cesar.\n8 – Descifrado utilizando cifrado Cesar.\n9 – Salir")
print ("")
print ("Ingrese la opción deseada")
x = input()
while "0"!= x and "1" != x and "2" != x and "3" != x and "4" != x and "5" != x and "6" != x and "7" != x and "8" != x and "9" != x:
    print ("La opción que Ud. ingresó no es válida")
    x = input("Ingrese la opción deseada")
x=int(x)

while x != 9:
    cadena_comparadora= "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ .,_1234567890><!#$%&/()=?¡¿´+*[]{}_:;áéíóú"     
    if x ==1:
        cadena = cadena.upper()
        print (cadena)
        x = int(input("Ingrese la opción deseada"))
        
    elif x ==2:
        cadena = cadena.title ()
        print (cadena)
        x = int(input("Ingrese la opción deseada"))
               
    elif x ==3:
        cadena = cadena.lower ()
        print (cadena)
        x = int(input("Ingrese la opción deseada"))
                
    elif x ==4 :
        cadena = cadena.lstrip()
        print (cadena)
        x = int (input("Ingrese la opción deseada"))

    elif x ==5 :
        cadena = cadena.rstrip()
        print (cadena)
        x = int (input("Ingrese la opción deseada"))
        
        
    elif x == 6 :
        modificado = input("Ingrese caracter o palabra a sustituir")
        modificador = input ("Ingrese caracter o palabra que sustituye")
        if modificado in cadena:
            cadena = cadena.split(modificado)
            cadena = modificador.join(cadena)
        else:
            print ("La palabra a sustituir no existe en la cadena")
        print (cadena)
        x = int(input("Ingrese la opción deseada"))

    elif x ==7:
        numeros = []
        for n in range (0,98):
            numeros.append(str(n))
            
        despl = input("Ingrese el desplazamiento de cifrado")
        while str(despl)not in numeros:
            print ("La opción que Ud. ingresó no es válida")
            despl = input("Ingrese el desplazamiento de cifrado")
        a = int(despl)
        cifrada = ""

        for i in range (len(cadena)):
            x= cadena_comparadora.find(cadena[i])
            while x+a >= 97:
                x -= 97
            cifrada += cadena_comparadora[x+a]
        cadena = cifrada
        print (cadena)
        x = int(input("Ingrese la opción deseada"))

    
    elif x ==8 :
        numeros = []
        for n in range (0,98):
            numeros.append(str(n))
            
        despl = input("Ingrese el desplazamiento de cifrado")
        while str(despl)not in numeros:
            print ("La opción que Ud. ingresó no es válida")
            despl = input("Ingrese el desplazamiento de cifrado")
        a = int(despl)
        cifrada = ""
        for i in range (len(cadena)):
            x= cadena_comparadora.find(cadena[i])
            while x+a >= 97:
                x -= 97
            cifrada += cadena_comparadora[x-a]
        cadena = cifrada
        print (cadena)
        x = int(input("Ingrese la opción deseada"))

    elif x == 0:
        comando = input ("Ingrese los comandos deseados: ")
        if comando == "menu":
            print ("")
            print ("MENU PRICIPAL")
            print ("")
            print ("0- Modo Comando\n1 – Cambiar todas las letras de minúsculas a MAYÚSCULAS.\n2 – Cambiar de minúscula a Mayúscula la primera letra de todas las palabras.\n3 – Cambiar de MAYÚSCULAS a minúsculas todas las letras.\n4 – Quitar todos los espacios a la izquierda del texto.\n5 – Quitar todos los espacios a la derecha del texto.\n6 – Reemplazar todas las ocurrencias de un carácter o palabra por otro\n7 – Cifrado utilizando cifrado Cesar.\n8 – Descifrado utilizando cifrado Cesar.\n9 – Salir")
            print ("")
            print ("Ingrese la opción deseada")
            x = int(input())
            while "0"!= str(x) and "1" != str(x) and "2" != str(x) and "3" != str(x) and "4" != str(x) and "5" != str(x) and "6" != str(x) and "7" != str(x) and "8" != str(x) and "9" != str(x):
                    print ("La opción que Ud. ingresó no es válida")
                    comando = input ("Ingrese los comandos deseados: ")
        if x ==0:
            comando = str(comando)
            comando = list(comando)
            comando = "".join(comando)
            comando = comando.split("|")
        
            intercambio = []
            cadena_comparadora= "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ .,_1234567890><!#$%&/()=?¡¿´+*[]{}_:;áéíóú"
            lista_abc = list(cadena_comparadora)
            for i in lista_abc:
                for j in lista_abc:
                    intercambio.append (str(str(i)+">"+str(j)))
            cif = []
            cif1= ["cif "]
            for i in cif1:
                for numero in range (0,98):
                    cif.append (str(str(i)+str(numero)))
            decif = []
            decif1= ["decif "]
            for i in decif1:
                for numero in range (0,98):
                    decif.append (str(str(i)+str(numero)))
        

            lista_de_comandos = ["mM","Mm","aA","-espacio","más>+","cif ","decif ","salir"]+ intercambio+cif+decif

            verificador = 0
            while verificador < len(comando):
                for i in range (len(comando)):
                    if comando[i] in lista_de_comandos:
                        verificador += 1
                    else:
                        print ("Error: Verifique los comandos ingresados")
                        comando = input ("Ingrese los comandos deseados: ")
                        comando = list(comando)
                        comando = "".join(comando)
                        comando = comando.split("|")


            for i in range (len(comando)):
            
                if comando[i] == "mM":
                    cadena = cadena.upper()

                elif comando[i]=="Mm":
                    cadena = cadena.lower()

                elif comando[i] == "aA":
                    cadena = cadena.title ()

                elif comando[i] == "-espacio":
                    cadena = cadena,strip()

                elif comando[i] in intercambio:
                    lista1 = comando[i]
                    lista1 = lista1.split(">")
                    aux = cadena.split(lista1[0])
                    aux2= lista1[1].join(aux)
                    cadena = aux2

                elif comando[i] == "más>+":
                    if "más" in cadena:
                        cadena = cadena.split("más")
                        cadena = "+".join(cadena)

                    else:
                        print ("La palabra a sustituir no existe en la cadena")
                        print ("")
                        print (cadena)

            
                elif comando [i] in cif:
                    cad = cadena
                    lista2=comando[i]
                    lista2=lista2.split("cif ")
                    lista3= lista2[1]
                    avance = int(lista3[0])
                               
                    cifrada = ""
                    cadena_comp= "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ .,_1234567890><!#$%&/()=?¡¿´+*[]{}_:;áéíóú"
               
                    for i in range (len(cadena)):
                        adelanto = cadena_comp.find(cad[i])
                        cifrada += cadena_comp [adelanto+avance]
                        cadena = cifrada
                    
                elif comando [i] in decif:
                    cad = cadena
                    lista2=comando[i]
                    lista2=lista2.split("decif ")
                    lista3= lista2[1]
                    avance = int(lista3[0])
                               
                    cifrada = ""
                    cadena_comp= "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ .,_1234567890><!#$%&/()=?¡¿´+*[]{}_:;áéíóú"
           
                    for i in range (len(cadena)):
                        adelanto = cadena_comp.find(cad[i])
                        cifrada += cadena_comp [adelanto-avance]
                        cadena = cifrada                
                elif comando [i] == "salir":
                    x = 9
                    



        if x == 0:
            print("")
            print (cadena)
        
print ("Usted ha finalizado el programa.")
