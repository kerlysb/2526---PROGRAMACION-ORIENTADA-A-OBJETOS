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

class Guerrero(Personaje):
    """
    Clase derivada: hereda de Personaje.
    Demuestra herencia y polimorfismo (sobrescribe atacar).
    """
    def __init__(self, nombre, vida):
        super().__init__(nombre, vida)
        self.__fuerza = 20  # Encapsulación adicional

    def atacar(self):
        """Polimorfismo: sobrescribe método de clase base."""
        print(f"{self.get_nombre()} (Guerrero) ataca con espada (20 dmg)!")

class Mago(Personaje):
    """
    Clase derivada: herencia y polimorfismo.
    """
    def __init__(self, nombre, vida):
        super().__init__(nombre, vida)
        self.__magia = 15

    def atacar(self):
        """Polimorfismo: implementación diferente."""
        print(f"{self.get_nombre()} (Mago) lanza bola de fuego (15 dmg)!")

# Demostración: instancias y métodos
if __name__ == "__main__":
    # Instancias de clases base y derivadas
    personaje_base = Personaje("Soldado", 100)
    guerrero = Guerrero("Danny", 150)
    mago = Mago("Merlín", 80)

    # Demostración de encapsulación: getters y setters
    print("=== Demostración de Encapsulación ===")
    personaje_base.mostrar_info()
    personaje_base.set_vida(90)
    print(f"Vida actualizada: {personaje_base.get_vida()}")

    print("\n=== Demostración de Herencia y Polimorfismo ===")
    # Herencia: clases derivadas usan método heredado
    guerrero.mostrar_info()
    mago.mostrar_info()

    # Polimorfismo: mismo método, comportamiento diferente
    print("\nAtaques:")
    personaje_base.atacar()  # Versión base
    guerrero.atacar()        # Sobrescrita
    mago.atacar()            # Sobrescrita

    # Lista polimórfica: funciona con cualquier subclase
    personajes = [personaje_base, guerrero, mago]
    for p in personajes:
        p.mostrar_info()
        p.atacar()
        print("---")