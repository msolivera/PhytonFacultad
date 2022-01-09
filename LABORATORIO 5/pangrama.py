def extraño (parametro):
    cadena1= parametro.lower()
    cadena2="abcdefghijklmnopqrstuvwxyzñ"
    contador=1
    for i in range (len(cadena2)):
        if cadena2[i] in cadena1:
            contador=contador+1
    if contador==28:
        return "PANGRAMA"
    else:
        return "nop" 
    

print(extraño("El viejo Señor Gómez pedía queso, kiwi y habas, pero le ha tocado un saxofón"))
