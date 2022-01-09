class fruta:
    
    def __init__ (self,nombre, calorias, vitamina_c, porcentaje_fibra, porcentaje_potasio):
        self.nombre = nombre
        self.calorias = calorias
        self.vitamina_c = vitamina_c
        self.porcentaje_fibra = porcentaje_fibra
        self.porcentaje_potasio = porcentaje_potasio

    def get_calorias(self):
        return self.calorias

    def set_calorias(self):
        return self.calorias

    def __repr__ (self):
        return "Nombre: " +self.nombre+" Calorias: "+str(self.calorias)+"K " +" Vitamina C: "+str(self.vitamina_c)+ "mm/kg ""Porcentaje de fibra: "+str(self.porcentaje_fibra)+"% "+" Porcentaje de Potasio: " +str(self.porcentaje_potasio)+"% "

    def engorda (self):
        if self.calorias>100:
            return "Verdadero"
        else:
            return "Falso"

    def nogripe (self):
        if self.vitamina_c > 0:
            return "Verdadero"
        else:
            return "Falso"

    

fruta1=fruta("banana",110,28,34,60)
fruta2=fruta("manzana",80,0,40,5)
fruta3=fruta("pera",90,8,37,8)
print(fruta1)
print(fruta2)
print(fruta3)
print("")
print(fruta1.engorda())
print(fruta2.engorda())
print(fruta3.engorda())
print("")
print(fruta1.nogripe())
print(fruta2.nogripe())
print(fruta3.nogripe())
    
    
