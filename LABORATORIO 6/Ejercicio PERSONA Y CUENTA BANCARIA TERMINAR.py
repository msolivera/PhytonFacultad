class persona:
    def __init__(self,nom,ap,ci,dire,tel):
        self.nombre=nom
        self.apellido=ap
        self.cedula=ci
        self.direccion=dire
        self.telefono=tel

    def __repr__ (self):
        return "Nombre: "+self.nombre+" Apellido: "+self.apellido+" Cedula: "+str(self.cedula)+" Diereccion: "+self.direccion+" Tel: "+str(self.telefono)

    def get_nombre (self):
        return self.nombre
    def get_apellino (self):
        return self.apellido
    def get_cedula (self):
        return self.cedula
    def get_direccion (self):
        return self.direccion
    def get_telefono (self):
        return self.telefono

    def set_nombre (self,nuevo_n):
        if len(nuevo_n)>=1:
            self.nombre=nuevo_n
    def set_apellino (self,nuevo_a):
        if len(nuevo_a)>=1:
            self.apellido=nuevo_a
    def set_direccion (self,nuevo_d):
        if len(nuevo_d)>=1:
            self.direccion=nuevo_d
    def set_telefono (self,nuevo_t):
        if len(nuevo_t)==8:
            self.telefono=nuevo_t
p1 = persona("Micaela","Olivera",52304220,"sebastopol 5665",25146676)
p2 = persona("Agustin","Picos", 53467540, "Av.italia",25146676)
print (p1)
print(p2)

class cbancaria:
    def __init__ (self, numero, dueño):
#saldo no lo pongo como parametro xq como arranca en cero no lo incluyo como parametro)
        self.numero=numero
        self.saldo=0
        self.dueño=dueño
    def __repr__(self):
        return "Numero de cuenta: " +str(self.numero)+ " Saldo disponible: " + str(self.saldo)+ " Usuario: " + str(self.dueño)

    def extraccion (self,extraccion):
        if self.saldo<extraccion:
            print ("Saldo insuficiente: no puede realizar esa operacion")
        elif self.saldo> extraccion:
            self.saldo=self.saldo-extraccion
    def deposito (self, deposito):
        self.saldo=self.saldo+deposito

    def transferencia(self, otra_cuenta,dinero):
        if self.saldo>dinero:
            self.saldo=self.saldo-dinero
            otra_cuenta.saldo=otra_cuenta.saldo+dinero
            print("Transaccion realizada con exito")
        else:
            print ("Saldo insuficiente: no puede realizar esa operacion")
    
        
    def get_saldo (self):
        return self.saldo
    def set_saldo (self,nuevo_saldo):
        if nuevo_saldo>=0:
            self.saldo=nuevo_saldo
        

cuenta1 = cbancaria(240,p1)
cuenta2 = cbancaria(241,p2)
print(cuenta1)
print (cuenta2)

cuenta1.set_saldo(1000) #añade saldo a cuenta deseada
cuenta2.set_saldo(1000)
print(cuenta1)
print(cuenta2)
cuenta1.transferencia(cuenta2,500)
print(cuenta1)
print(cuenta2)
cuenta1.extraccion() #extraccion: si la misma es mayor al saldo disponible salta un error
cuenta1.deposito() #añade dinero a la cuenta deseada




















