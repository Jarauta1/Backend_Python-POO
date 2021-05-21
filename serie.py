import interfaz

class Serie(interfaz.Entregable):
    # Propiedades
    __titulo = ""
    __temporadas = 3
    entregado = False
    __genero = ""
    __creador = ""

    # Constructor
    def __init__(self, titulo, genero, creador, temporadas = 3):
        self.__titulo = titulo
        self.__genero = genero
        self.__creador = creador
        self.__temporadas = temporadas

    # Métodos mágicos
    def __str__(self):
        out = "Serie: \n Titulo: {0} - Temporadas: {1} - Genero: {2} - Creador: {3}" #Estructura para mostrar la info de la serie
        return out.format(self.titulo, self.temporadas, self.genero, self.creador) #Completar la info de salida con las propiedades

    # Get / Set
    @property
    def titulo(self):
        return self.__titulo

    @property
    def temporadas(self):
        return self.__temporadas

    @property
    def genero(self):
        return self.__genero

    @property
    def creador(self):
        return self.__creador

    @titulo.setter
    def cambiar_titulo(self, titulo):
        self.__titulo = titulo

    @temporadas.setter
    def cambiar_temporadas(self, temporadas):
        self.__temporadas = temporadas

    @genero.setter
    def cambiar_genero(self, genero):
        self.__genero = genero

    @creador.setter
    def cambiar_creador(self, creador):
        self.__creador = creador

    # Métodos
