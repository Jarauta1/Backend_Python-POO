class Asignatura():
    # Propiedades
    __id = 0 # Añadido kata_04
    nombre = ""
    nota = 0 # Modificado kata_04 de nota a __nota


    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre

    # Añadido kata_04
    # Get / Set
    @property
    def nota(self):
        return self.__nota

    @property
    def id(self):
        return self.__id

    # Método
    def anyadir_nota(self, nota):
        if (nota <= 10 and nota >= 0):
            self.nota = nota