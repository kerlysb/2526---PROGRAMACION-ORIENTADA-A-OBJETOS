# Técnica de encapsulación
#Se protegen atributos usando la convención de subrayado y se accede mediante getters/setters
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre      # "protegido"
        self._edad = edad          # "protegido"

    # Getter
    def get_edad(self):
        return self._edad

    # Setter con validación
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad no puede ser negativa")

    def mostrar(self):
        print(f"{self._nombre} tiene {self._edad} años")


p = Persona("Luis", 20)
p.mostrar()
p.set_edad(25)
p.mostrar()
p.set_edad(-5)   # No permite valor negativo