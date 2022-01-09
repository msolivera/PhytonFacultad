def trasformar_nombre(lista):
    resultado=[]
    for elem in lista:
        nombre=" ".join(elem)
        resultado.append(nombre)
    return resultado
transformar_nombre(["micaela","olivera","jorge","llagarias"])
