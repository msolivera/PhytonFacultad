class personaje:
    def __init__ (self,nombre,vida,poder,daño): #init siempre para poder definir que compone a mi clase
        self.nombre=nombre
        self.vida=vida
        self.poder=poder
        self.daño=daño
    def __repr__ (self): #para poder representarlo
        return "Nombre: " + self.nombre + " Vida: " +str(self.vida)+ " Poder: " + self.poder +" daño: " +str(self.daño)
    def atacar(self, otro_personaje):
        otro_personaje.vida=otro_personaje.vida-self.daño

per1 = personaje ("Pikachu",100,"impactrueno",50)
per2 = personaje ("vaporeon",200,"chorro de agua",10)
per3 = personaje ("executor",100,"hiperrayo",30
per1.atacar(per2)



                  
