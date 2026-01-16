"""
Programa de demostración de conceptos POO en Python:
- Herencia: Clase Personaje (base) y Guerrero/Mago (derivadas).
- Encapsulación: Atributos privados con __ (name mangling) y métodos getter/setter.
- Polimorfismo: Método atacar() sobrescrito en clases derivadas.
"""
class Personaje:
    """
    Clase base: demuestra encapsulación con atributos privados.
    """
    def __init__(self, nombre, vida):
        # Encapsulación: atributos privados con __
        self.__nombre = nombre
        self.__vida = vida

    # Getter para nombre (encapsulación)
    def get_nombre(self):
        return self.__nombre

    # Getter para vida
    def get_vida(self):
        return self.__vida

    # Setter para vida (con validación)
    def set_vida(self, nueva_vida):
        if nueva_vida >= 0:
            self.__vida = nueva_vida

    def mostrar_info(self):
        """Método base para mostrar información."""
        print(f"{self.get_nombre()}: Vida = {self.get_vida()}")

    def atacar(self):
        """Método base para polimorfismo (será sobrescrito)."""
        print(f"{self.get_nombre()} ataca con fuerza básica (10 dmg).")

