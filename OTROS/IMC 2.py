def imc (peso,altura):
    valor = peso / altura **2
    if valor <18:
        return "Delgadez"
    elif valor <25:
        return "Normal"
    elif valor <29:
        return "Sobrepeso"
    else:
        return "Obesidad"
 
valor_imc = imc (58,1.55)
print (valor_imc)

