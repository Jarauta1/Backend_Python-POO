class Animal():
    # Propiedades
    especie = ""
    altura = ""
    peso = ""

    # Constructor
    def __init__(self, especie, altura, peso):
        self.especie = especie
        self.altura = altura
        self.peso = peso

    # Get / Set

    # Métodos
    def comer(self):
        print("Estoy comiendo")

    def cazar(self):
        print("Voy a cazar")

    def dormir(self):
        print("Voy a dormir")


class Leon(Animal):
    # Propiedades

    # Constructor
    def __init__(self, altura, peso):
        super().__init__("Leon", altura, peso)

    # Get / Set

    # Métodos


class Mascota():
    # Propiedades
    nombre = ""
    amo = ""

    # Constructor
    def __init__(self, nombre, amo):
        self.nombre = nombre
        self.amo = amo

    # Get / Set

    # Métodos
    def sentarse(self):
        print("Estoy sentado")

    def dar_pata(self):
        print("Te doy la pata")


class Perro(Animal, Mascota):
    # Propiedades

    # Constructor
    def __init__(self, nombre, amo, altura, peso):
        Animal.__init__(self, "Perro", altura, peso)
        Mascota.__init__(self, nombre, amo)

    # Get / Set

    # Métodos
if __name__ == '__main__':
    rocky = Perro("Rocky", "Diego", 0.5, 25)

    rocky.cazar()
    rocky.dormir()
    rocky.sentarse()
    print(rocky.nombre)
    print(rocky.especie)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/