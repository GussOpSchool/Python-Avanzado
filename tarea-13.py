from abc import ABC, abstractmethod

class Animal(ABC):
      def __init__(self, especie, edad):
            self.especie = especie
            self.edad = edad

      @abstractmethod
      def hablar(self):
            return "Este animal dice: "
      
      @abstractmethod
      def moverse(self):
            return "Este animal se mueve "

      def quiensoy(self):
            return "Este animal es "

class Delfin(Animal):
      def hablar(self):
            return super().hablar() + "chasquido"
      
      def moverse(self):
            return super().moverse() + "nadando"
      
      def quiensoy(self):
            return super().quiensoy() + "acuatico"

class Abeja(Animal):
      def hablar(self):
            return super().hablar() + "bzzzzzzzz"
      
      def moverse(self):
            return super().moverse() + "volando"

      def quiensoy(self):
            return super().quiensoy() + "insecto"
      
      def picar(self):
            return "La abeja te pica!"

class Caballo(Animal):
      def hablar(self):
            return "Este animal dice: trotrotro"
      
      def moverse(self):
            return "Este animal se mueve trotando"
      
      def quiensoy(self):
            return super().quiensoy() + "equino"

class Humano(Animal):
      def __init__(self, nombre, edad):
            super().__init__("Humano", edad)
            self.nombre = nombre

      def hablar(self):
            return "Este animal dice: Hola!"
      
      def moverse(self):
            return "Este animal se mueve caminando"
      
      def quiensoy(self):
            return super().quiensoy() + "mamifero"

class Nino(Humano):
      def __init__(self, nombre, edad, padres):
            super().__init__(nombre, edad)
            self.padres = list(padres)

      def nombrepadres(self):
            print("Sus padres son:" + ", ".join(self.padres))

      def llorar(self):
            return "el niño llora: 'buaaaaaaa'"

class Centauro(Caballo, Humano):
      def __init__(self, nombre, edad):
            Humano.__init__(self, nombre, edad)
            self.especie = "Centauro"

      def hablar(self):
            return Humano.hablar(self)
      
      def moverse(self):
            return Caballo.moverse(self)

      def quiensoy(self):
            return "Este animal es hibrido"
      
class Show:
      def hablar(self):
            return "La banda toca sus instrumentos"

      def moverse(self):
            return "El show no se mueve" 

      def quiensoy(self):
            return "Somos muchos artistas"

animales = [
      Caballo("Caballo",  10),
      Delfin("Delfin", 15),
      Abeja("Abeja Reina", 2),
      Humano("Gustavo", 16),
      Nino("Juanito", 3, ["Juana", "Juan"]),
      Centauro("Eurian", 40),
      Show()
]

for animal in animales:
      print(animal.hablar())
      print(animal.moverse())
      print(animal.quiensoy())
      print("")