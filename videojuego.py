import interfaz

class Videojuego(interfaz.Entregable):
    # Propiedades
    __titulo = ""
    __horas = 10
    entregado = False
    __genero = ""
    __companyia = ""

    # Constructor
    def __init__(self, titulo, genero, companyia,horas = 10):
        self.__titulo = titulo
        self.__genero = genero
        self.__companyia = companyia
        self.__horas = horas

    # Métodos mágicos
    # toString()
    def __str__(self):
        out = "Videojuego: \n Titulo: {0} - Horas: {1} - Genero: {2} - Compañía: {3}"
        return out.format(self.titulo, self.horas, self.genero, self.companyia)

    # Get / Set
    @property
    def titulo(self):
        return self.__titulo

    @property
    def horas(self):
        return self.__horas

    @property
    def genero(self):
        return self.__genero

    @property
    def companyia(self):
        return self.__companyia

    @titulo.setter
    def cambiar_titulo(self, titulo):
        self.__titulo = titulo

    @horas.setter
    def cambiar_horas(self, horas):
        self.__horas = horas

    @genero.setter
    def cambiar_genero(self, genero):
        self.__genero = genero

    @companyia.setter
    def cambiar_companyia(self, companyia):
        self.__companyia = companyia

    # Métodos
    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return print(self.entregado)

    def compareTo(self):
        pass