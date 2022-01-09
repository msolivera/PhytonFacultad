class hora:
    def __init__ (self):
        self.hora=0
        self.minuto=0
        self.segundo=0
    
#hasta ahora poniamos los parametro pero esta nos pida q tenga los valores 0 por omision,
#sinosotros sabemos q los valores son 0 n tiene sentido q recibamos los parametros.
    def validar (self):
        if not (self.hora<24 and self.hora>=0 and self.minuto<60 and self.minuto>=0 and self.segundo<60 and self.segundo>=0):
            self.hora=0
            self.minuto=0
            self.segundo=0
    def __repr__ (self):
        return "hora: " +str(self.hora)+ " minutos: " +str(self.minuto)+ " segundos:" +str(self.segundo)
    def asegundos (self):
        return self.hora*3600+self,minutos*60+self.segundo
    def desegundos (self, x):
        self.hora=x//3600
        self.minuto=(x-self.hora*3600)//60
        self.segundo= x-self.hora*3600-self.minuto*60

    def clonar (self):
        resultado=hora()
        resultado.hora = self.hora=0
        resultado.minuto = self.minuto=0
        resultado.segundo = self.segundo=0

        return resultado
    
    def __eq__(self,otro):
        return self.hora==otro.hora and self.minuto==otro.minuto and self.segundo==otro.segundo
#para comparar objetos

hora1=hora()
hora1.hora=2
hora1.minuto=24
hora1.segundo=30
hora2=hora()
hora2.hora=2
hora2.minuto=24
hora2.segundo=30
print(hora1)
print(hora2)
print(hora1==hora2)
horax=hora1.clonar()
print (horax)
#si no tengo la fucion eq python nos va a decir q no son iguales ya que son objetos distintos
#eq sirve para decirnos si ambos objetos son iguales en sus propiedades o parametros


#para clonar una hora:

