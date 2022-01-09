class personaje:
    def __init__ (self,nombre,vida,poder,daño):
        self.nombre=nombre
        self.vida=vida
        self.poder=poder
        self.daño=daño
    def __repr__(self):
        return "Nombre: "+self.nombre+ " vida: "+str(self.vida)+ " Poder: "+self.poder+ " Daño: "+str(self.daño)
        
    def atacar(self, otro_personaje):
        otro_personaje.vida=otro_personaje.vida-self.daño
    def atacar2(self, otro1, otro2):
        otro1.vida-=self.daño
        otro2.vida-=self.daño
    def atacar3 (self,ataca2,otro_personaje):
        otro_personaje.vida= otro_personaje.vida-ataca2.daño-self.daño
    def tiene_vida(self):
        return self.vida>0
    def get_vida (self):
        return self.vida
    def set_vida (self, nueva_vida):
        if nueva_vida>=0 and nueva_vida<= 100:
            self.vida=nueva_vida
        
    
#se usa str para los elementos que son numeros y que van a ser representados coo tal
per1= personaje("Link" ,100,"patada",20)
per2= personaje("zelda",100,"piña",25)
per3= personaje("Pikachu",120,"Impactrueno",30)
per3.atacar(per1)

per1.atacar2(per2,per3) #para ataquar a dos a la vez


per1.set_vida(50) #para modificar la vida mediante el set
print (per1)
per1.set_vida(200) #si le pongo una vida que no esta contemprada dentro del set no la modifica
print(per1)
