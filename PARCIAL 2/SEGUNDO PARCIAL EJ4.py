class libro ():
    def __init__ (self, titulo, autor, paginas, editorial, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.editorial = editorial
        self.ISBN = ISBN

    def __repr__ (self):
        return "Titulo: " + self.titulo +","+ " Autor: " + self.autor +","+ " Paginas: " + str(self.paginas) +","+ " Editorial: " + self.editorial +","+ " Numero ISBN: " + self.ISBN+"."

    def mismo_autor(self,lista):
        resultado = []
        for libro in lista:
            if libro[1]=="Gabriel Garcia Marquez":
                resultado.append(libro)
        return resultado
            
    def largo(self):
        return self.paginas > 500

libro1=libro("Cuentos para niños","Gabriel Garcia Marquez",400,"ED.Amanecer","mkl675")
libro2=libro("Programacion 1","Juan Perez",800,"ED.Amanecer","mkl675")
libro3=libro("Analisis Matematico","Juan Perez",600,"ED.Amanecer","mkl675")
libro4=libro("Cuentos para niños","Maria Cardozo",600,"ED.Amanecer","mkl675")
libro5=libro("Cuentos para niños2","Gabriel Garcia Marquez",600,"ED.Amanecer","mkl675")
print(libro1)
print("")
print(libro1.largo())
print("")
print(libro2.largo())
print("")
print(libro1.mismo_autor([("Cuentos para niños","Gabriel Garcia Marquez",400,"ED.Amanecer","mkl675"),("Programacion 1","Juan Perez",800,"ED.Amanecer","mkl675"),("Analisis Matematico","Juan Perez",600,"ED.Amanecer","mkl675"),("Cuentos para niños","Maria Cardozo",600,"ED.Amanecer","mkl675"),("Cuentos para niños2","Gabriel Garcia Marquez",600,"ED.Amanecer","mkl675")]))
