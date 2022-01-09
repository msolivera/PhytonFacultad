#definimos bloque como conjunto de lineas que poseen una funcion
#bloque OPIN: Este tipo de bloque es utilizado para que el usuario no ingrese opciones incorrectas

# Presentación del programa
print ("BIENVENIDO AL PROGRAMA DE TRANSFORMACION DE CADENAS")
print ("")
print ("Ingrese a continuación la cadena de caracteres que desea modificar:")

cadena = input()    #ingreso de la cadena a editar
Cadena_Inicial = cadena
#bloque que impide que se ingrese una cadena de longitud 0

while len(cadena) == 0:     
    print ("Debe ingresar al menos un caracter")
    cadena = input()    #se solicita nuevamente la cadena

#definicion de menu, opciones y cadena comparadora para utilizar más adelante

menu = "MENU PRICIPAL\n\n0- Modo Comando\n1 – Cambiar todas las letras de minúsculas a MAYÚSCULAS.\n2 – Cambiar de minúscula a Mayúscula la primera letra de todas las palabras.\n3 – Cambiar de MAYÚSCULAS a minúsculas todas las letras.\n4 – Quitar todos los espacios a la izquierda del texto.\n5 – Quitar todos los espacios a la derecha del texto.\n6 – Reemplazar todas las ocurrencias de un carácter o palabra por otro\n7 – Cifrado utilizando cifrado Cesar.\n8 – Descifrado utilizando cifrado Cesar.\n9 – Salir\n10- Mostrar MENU\n11- Contacto"

opciones = ["0","1","2","3","4","5","6","7","8","9","10","11"]        

cadena_comparadora= "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ .,_1234567890><!#$%&/()=?¡¿´+*[]{}_:;áéíóú"

x = 10  #definimos la opcion inicial "10" para que el programa inicie con el menú

while x != 9:   #mientras la opciion ingresada no sea la salida, se produce un bucle que permite hacer varias modificaciones a la cadena
    if x==11 : #contacto
        print ("")
        print ("Contacto:\nPor consultas comuníquese via mail con nosotros: Micaela Olivera (micaela.olivera@correo.ucu.edu.uy) , Agustin Picos(agustin.picos@correo.ucu.edu.uy)\nMuchas gracias")
        opcion = input("Ingrese la opción deseada: ")
        #OPIN
        while opcion not in opciones:
            print ("La opción que Ud. ingresó no es válida")
            opcion = input("Ingrese la opción deseada: ")
        x = int(opcion)
    elif x == 10: #mostrar menu
        print ("")
        print (menu)
        opcion = input("Ingrese la opción deseada: ")
        #OPIN
        while opcion not in opciones:
            print ("La opción que Ud. ingresó no es válida")
            opcion = input("Ingrese la opción deseada: ")
        x = int(opcion)

    elif x == 1:    #opcion 1
        cadena = cadena.upper()
        print (cadena)
        opcion = input("Ingrese la opción deseada: ")
        #OPIN
        while opcion not in opciones:
            print ("La opción que Ud. ingresó no es válida")
            opcion = input("Ingrese la opción deseada: ")
        x = int(opcion)

    elif x ==2:    #opcion 2
        cadena = cadena.title ()
        print (cadena)
        opcion = input("Ingrese la opción deseada: ")
        #OPIN
        while opcion not in opciones:
            print ("La opción que Ud. ingresó no es válida")
            opcion = input("Ingrese la opción deseada: ")
        x = int(opcion)
               
    elif x ==3:    #opcion 3
        cadena = cadena.lower ()
        print (cadena)
        opcion = input("Ingrese la opción deseada: ")
        #OPIN
        while opcion not in opciones:
            print ("La opción que Ud. ingresó no es válida")
            opcion = input("Ingrese la opción deseada: ")
        x = int(opcion)
        
    elif x ==4 :    #opcion 4
        cadena = cadena.lstrip()
        print (cadena)
        opcion = input("Ingrese la opción deseada: ")
        #OPIN
        while opcion not in opciones:
            print ("La opción que Ud. ingresó no es válida")
            opcion = input("Ingrese la opción deseada: ")
        x = int(opcion)
        
    elif x ==5 :    #opcion 5
        cadena = cadena.rstrip()
        print (cadena)
        opcion = input("Ingrese la opción deseada: ")
        #OPIN
        while opcion not in opciones:
            print ("La opción que Ud. ingresó no es válida")
            opcion = input("Ingrese la opción deseada: ")
        x = int(opcion)
        
        
    elif x == 6 :    #opcion 6
        modificado = input("Ingrese caracter o palabra a sustituir ")
        modificador = input ("Ingrese caracter o palabra que sustituye ")
        if modificado in cadena:
            cadena = cadena.split(modificado)
            cadena = modificador.join(cadena)
        #OPIN
        else:
            print ("La palabra a sustituir no existe en la cadena")
        print (cadena)
        opcion = input("Ingrese la opción deseada: ")
        #OPIN
        while opcion not in opciones:
            print ("La opción que Ud. ingresó no es válida")
            opcion = input("Ingrese la opción deseada: ")
        x = int(opcion)

    elif x ==7:    #opcion 7
        numeros = []
        for n in range (0,98):
            numeros.append(str(n))
            
        despl = input("Ingrese el desplazamiento de cifrado ")
        #OPIN
        while str(despl)not in numeros:
            print ("La opción que Ud. ingresó no es válida")
            despl = input("Ingrese el desplazamiento de cifrado ")
        a = int(despl)

        cifrada = ""

        for i in range (len(cadena)):
            x= cadena_comparadora.find(cadena[i])
            while x+a >= 97:    #en esta opcion, se puede ingresar un valor de cifrado mayor a 97
                x -= 97
            cifrada += cadena_comparadora[x+a]
        cadena = cifrada
        print (cadena)
        opcion = input("Ingrese la opción deseada: ")
        #OPIN
        while opcion not in opciones:
            print ("La opción que Ud. ingresó no es válida")
            opcion = input("Ingrese la opción deseada: ")
        x = int(opcion)

    
    elif x ==8 :    #opcion 8
        numeros = []
        for n in range (0,98):
            numeros.append(str(n))
            
        despl = input("Ingrese el desplazamiento de cifrado")
        #OPIN
        while str(despl)not in numeros:
            print ("La opción que Ud. ingresó no es válida")
            despl = input("Ingrese el desplazamiento de cifrado ")
        a = int(despl)
        cifrada = ""
        for i in range (len(cadena)):
            x= cadena_comparadora.find(cadena[i])
            while x+a >= 97:    #en esta opcion, se puede ingresar un valor de cifrado mayor a 97
                x -= 97
            cifrada += cadena_comparadora[x-a]
        cadena = cifrada
        print (cadena)
        opcion = input("Ingrese la opción deseada: ")
        #OPIN
        while opcion not in opciones:
            print ("La opción que Ud. ingresó no es válida")
            opcion = input("Ingrese la opción deseada: ")
        x = int(opcion)

    elif x == 0:    #opcion 0
        print("Modo Comando")
        comando = input ("Ingrese los comandos deseados: ")#el comando es de tipo (str)
        if comando == "10":
            x = 10

        else:
            comando = str(comando)
            comando = list(comando)
            comando = "".join(comando)
            comando = comando.split("|")

            #Bloque intercambio / se crea la lista"intercambio" que posee todas las combinaciones
            #de la cadena comparadora (todos los caracteres), consigo misma, concatenados por el caracter ">"
            intercambio = []
            lista_abc = list(cadena_comparadora)
            for i in lista_abc:
                for j in lista_abc:
                    intercambio.append (str(str(i)+">"+str(j)))

            #Bloque cif / se crea la lista cif que posee todas las opciones de (cif x) hasta el valor maximo
            #de caracteres que posee la cadena comparadora
            # en este comando no está permtido realizar cifrados con un valor mayor a 97
            cif = []
            cif1= ["cif "]
            for i in cif1:
                for numero in range (0,98):
                    cif.append (str(str(i)+str(numero)))

            #Bloque decif / idem Bloque cif, para decifrados
            decif = []
            decif1= ["decif "]
            for i in decif1:
                for numero in range (0,98):
                    decif.append (str(str(i)+str(numero)))
        

            lista_de_comandos = ["mM","Mm","aA","-espacio","más>+","cif ","decif ","salir"]+ intercambio+cif+decif

            #OPIN - El verificador se utiliza para recorrer los comandos ingresados
            #       si la entrada es incorrecta, (verificador < len (comando)) se deben ingresar nuevamente
            verificador = 0
            while verificador < len(comando):
                for i in range (len(comando)):
                    if comando[i] in lista_de_comandos:##################################################################################################
                        verificador += 1
                    else:
                        print ("Error: Verifique los comandos ingresados")
                        comando = input ("Ingrese los comandos deseados: ")
                        comando = list(comando)
                        comando = "".join(comando)
                        comando = comando.split("|")#quitamos los "pipe" para obtener solamente los comandos

            for i in range (len(comando)):  #se recorren los comandos ingresados para proceder en orden de ingreso
            
                #opciones del modo comando/se compara el elemento recorrido con las opciones
                if comando[i] == "mM":
                    cadena = cadena.upper()

                elif comando[i]=="Mm":
                    cadena = cadena.lower()

                elif comando[i] == "aA":
                    cadena = cadena.title ()

                elif comando[i] == "-espacio":
                    cadena = cadena.strip()

                elif len(comando[i]) == 3 and comando[i][1] == ">":
                    lista1 = comando[i]################################################################################################################
                    lista1 = lista1.split(">")
                    aux = cadena.split(lista1[0])
                    aux2= lista1[1].join(aux)
                    cadena = aux2###################################################################################################################

                elif comando[i] == "más>+":
                    if "más" in cadena:
                        cadena = cadena.split("más")
                        cadena = "+".join(cadena)
                    #OPIN - en caso de que la cadena no contenga la palabra más (con tilde)
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
                                  
                    for i in range (len(cadena)):
                        adelanto = cadena_comparadora.find(cad[i])
                        cifrada += cadena_comparadora [adelanto+avance]
                        cadena = cifrada
                    
                elif comando [i] in decif:
                    cad = cadena
                    lista2=comando[i]
                    lista2=lista2.split("decif ")
                    lista3= lista2[1]
                    avance = int(lista3[0])
                    cifrada = ""
                    
                    for i in range (len(cadena)):
                        adelanto = cadena_comparadora.find(cad[i])
                        cifrada += cadena_comparadora [adelanto-avance]
                        cadena = cifrada

                #salida / el único comando restante es "salir".
                else:
                    x = 9


			x=int(cadena)
			xx=int(Cadena_Inicial)
            print("")
            print (cadena)



    else:
        print ("La opción que Ud. ingresó no es válida")
        opcion = input("Ingrese la opción deseada: ")
        #OPIN
        while opcion not in opciones:
            print ("La opción que Ud. ingresó no es válida")
            opcion = input("Ingrese la opción deseada: ")
        x = int(opcion)
            

print ("Usted ha finalizado el programa.")
print ("Cadena Inicial",(xx)
print ("Cadena final",(x)

