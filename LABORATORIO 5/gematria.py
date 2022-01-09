def gematria(subcadena):
    abecedario=subcadena.lower()
    contador=0
    cadena="abcdefghijklmnñopqrstuvwxyz"
    for i in range (len(abecedario)):
        x=cadena.find(abecedario[i])
        contador=contador+(x+1)

    return contador

print(gematria("aaa bbb"))
