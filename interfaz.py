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
        global mayor_horas
        global mayor_temporadas
        mayor_num = 0
        mayor_temporadas = 0
        global num_eval
        for key,value in object.items():
            if(value == 6):
                print("modern")

