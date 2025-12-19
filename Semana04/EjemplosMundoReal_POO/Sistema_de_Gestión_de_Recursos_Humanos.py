# Clase base Empleado - herencia común
class Empleado:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self._id_empleado = id_empleado  # Encapsulación
        self._salario_base = 0

    def calcular_salario(self):
        """Método que se sobrescribe - polimorfismo"""
        return self._salario_base

    def descripcion(self):
        return f"Empleado: {self.nombre} (ID: {self._id_empleado})"

# Clase Desarrollador - herencia simple
class Desarrollador(Empleado):
    def __init__(self, nombre, id_empleado, lenguaje):
        super().__init__(nombre, id_empleado)
        self.lenguaje = lenguaje
        self._salario_base = 2500

    def calcular_salario(self):
        """Polimorfismo: salario con bono por lenguaje"""
        bono = 500 if self.lenguaje == "Python" else 200
        return self._salario_base + bono
