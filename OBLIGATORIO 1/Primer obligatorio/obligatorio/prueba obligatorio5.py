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
x = str(input())
while "0"!= str(x) and "1" != str(x) and "2" != str(x) and "3" != str(x) and "4" != str(x) and "5" != str(x) and "6" != str(x) and "7" != str(x) and "8" != str(x) and "9" != str(x):
    print ("La opción que Ud. ingresó no es válida")
    x = input()

comando = input ("Ingrese los comandos deseados: ")
comando = list(comando)
comando = "".join(comando)
comando = comando.split("|")

intercambio = []
cadena_comparadora= "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ .,_1234567890><!#$%&/()=?¡¿´+*[]{}_:;áéíóú"
lista_abc = list(cadena_comparadora)
for i in lista_abc:
    for j in lista_abc:
        intercambio.append (str(str(i)+">"+str(j)))
lista_de_comandos = ["mM","Mm","aA","-espacio","mas>+","cif x","decif x"]+ intercambio

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
