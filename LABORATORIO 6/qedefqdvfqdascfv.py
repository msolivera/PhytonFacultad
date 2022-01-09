class hora:
    def __init__ (self):
        self.hora=0
        self.minuto=0
        self.segundo=0
    def __repr__ (self):
        return "hora: " +str(self.hora)+ " minutos: " +str(self.minuto)+ " segundos:" +str(self.segundo)
    def validar (self):
        if self.hora>24 or self.minuto>60 or self.segundo>60:
            print ("error")

hora1=hora()
hora1.hora=3546524
hora1.minuto=325
hora1.segundo=234567
print(hora1)


