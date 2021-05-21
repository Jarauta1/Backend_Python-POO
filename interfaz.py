class Entregable:

    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return print(self.entregado)

    def compareTo(self, object):
        global mayor_serie
        global mayor_videojuego
        mayor_temporadas = 0
        mayor_horas = 0

        #Buscamos en el array las series y/o videojuegos
        for element in object:
            if (hasattr(element,"temporadas") == True): #Filtro para comprobar que lo que evaluamos son series
                num = element.temporadas
                if num > mayor_temporadas: #Si damos con una serie que tiene más temporadas que lo almacenado:
                    mayor_temporadas = num #Guardamos su número de temporadas
                    mayor_serie = element #Y guardamos la serie para mostrarla al final
                else:
                    num = 0
            elif (hasattr(element,"horas") == True): #Filtro para comprobar que lo que evaluamos son videojuegos
                num = element.horas
                if num > mayor_horas: #Si damos con un videojuego que tiene más horas que lo almacenado:
                    mayor_horas = num #Guardamos su número de horas
                    mayor_videojuego = element #Y guardamos el videojuego para mostrarlo al final
                else:
                    num = 0

        #Si hemos analizado las series, mostramos la que más temporadas tiene
        if (hasattr(element,"temporadas") == True):
            return print(f'La serie que más temporadas tiene es: \n {mayor_serie}')
        # Si hemos analizado los videojuegos, mostramos el que más horas tiene
        elif (hasattr(element,"horas") == True):
            return print(f'El videojuego que más temporadas tiene es: \n {mayor_videojuego}')