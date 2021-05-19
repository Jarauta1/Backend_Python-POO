class Entregable:

    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return print(self.entregado)

    def compareTo(self):
        pass