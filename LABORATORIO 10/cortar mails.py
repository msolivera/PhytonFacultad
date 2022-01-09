def cortar(lista):
    destinatario=[]
    copia=[]
    copia_oculta=[]
    
    for elem in lista:
        
        elem=elem.split("@")
        
        
        if elem[1]=="ucu.edu.uy":
            destinatario.append("@".join(elem))
            return "destinatario" ,destinatario

        if elem[1]=="gmail.com":
            copia.append("@".join(elem))
            return "copia", copia

        else:
            copia_oculta.append("@".join(elem))
            return "copia_o", copia_oculta
    
lista1=["molivera@ucu.edu.uy","molivera@gmail.com","molivera@yahoo.com","molivera@hotmail.com"]            

print(cortar(lista1))
