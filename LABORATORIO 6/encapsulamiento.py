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
    def get_daño(self):
        return self.daño
    def set_daño(self,nuevo_daño):
        if nuevo_daño>=0 and nuevo_daño<=50:
            self.daño=nuevo_daño
    def get_nombre(self):
        return self.nombre
    def set_nombre (self, nuevo_nombre):
        if len(nuevo_nombre)>=1 and len(nuevo_nombre)<=8:
            self.nombre=nuevo_nombre
        
        
    
#se usa str para los elementos que son numeros y que van a ser representados coo tal
per1= personaje("Link" ,100,"patada",20)
per2= personaje("zelda",100,"piña",25)
per3= personaje("Pikachu",100,"Impactrueno",50) 


per3.set_vida(500)
per3.set_daño(60)
per3.set_nombre("vnosdbhugeqhgoqehighoqierghoieqgwiphgo")
per3.set_poder(hola)
print (per3)
