
#A)
class RegistroSismico():
    def __init__ (self, latitud, longitud, dia, mes, año, hora, minuto, segundo, onda_p, onda_s):

        self.latitud = latitud
        self.longitud = longitud
        self.dia = dia
        self.mes = mes
        self.año = año
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        self.onda_p = onda_p
        self.onda_s = onda_s

    def get_latitud (self):
        return self.latitud
    def set_latitud (self):
        if self.latitud>90 or self.latitud>-90:
            self.latitud == 0
        return self.latitud
    
    def get_longitud (self):
        return self.longitud
    def set_longitud (self):
        if longitud>90 or longitud>-90:
            self.longitud == 0
    
    def get_dia (self):
        return self.dia
    def set_dia (self):
        if self.mes== 3 or self.mes== 5 or self.mes== 7 or self.mes== 8 or self.mes== 10 or self.mes== 12 and self.dia>30:
            self.dia==0
        elif self.mes== 1 or self.mes== 2 or self.mes== 4 or self.mes== 6 or self.mes== 9   or self.mes== 11 and self.dia>31:
            self.dia==0 
    
    def get_mes (self):
        return self.mes
    def set_mes (self):
        if self.mes >12:
            self.mes== 0

    def get_año (self):
        return self.año
    
    def get_hora (self):
        return self.hora
    def set_hora (self):
        if self.hora >24:
            self.hora== 0
    
    def get_minuto (self):
        return self.minuto
    def set_minuto (self):
        if self.minuto >60:
            self.minuto== 0
    
    def get_segundo(self):
        return self.segundo
    def set_segundo (self):
        if self.segundo >60:
            self.segundo== 0

    def get_onda_p(self):
        return self.onda_p

    def get_onda_s(self):
        return self.onda_s


    def __repr__ (self):
        return "REGISTRO SISMICO: Latitud: " + str(self.latitud) + " Longitud : " + str(self.longitud) + " Dia: " + str(self.dia) + " Mes: " + str(self.mes) + " Año: " + str(self.año) + " Hora: " + str(self.hora) + " Minutos: " + str(self.minuto) + " Segundos: " + str(self.segundo) + " Onda P: " + str(self.onda_p) + " Onda S: " + str(self.onda_s)
    

#B)
    def cargar_datos (nombre_archivo):

        archivo = open (nombre_archivo , "r")

        lista_datos =[]

        for linea in archivo:

            dato = linea.strip().split(",")

            lista = RegistroSismico(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8],dato[9])

            lista_datos.append(lista)

        archivo.close()

        return lista_datos



#D)
    def cargar_archivos(lista_archivos):

        registros = []

        for elemento in lista:

            archivo = open (elemento, "r")

            for lineas in archivo:

                datos = lineas.strip().split()

            listas = RegistroSismico ( datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9])

            registros.append(listas)

        archivo.close()

        return registros

        

            

        
registro1= RegistroSismico (89 , -23, 23, 4, 3, 23,56,34,0.23,0.25)
print(registro1)

datos1=RegistroSismico.cargar_datos("c:\\temp\\sismicos.csv")
print(datos1)

    

















    
