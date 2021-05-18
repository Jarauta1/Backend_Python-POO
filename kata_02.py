class Asignatura():
    # Propiedades
    nombre = ""
    nota = 0

    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre

    # Método
    def anyadir_nota(self, nota):
        if (nota <= 10 and nota >= 0):
            self.nota = nota