# Clase base Empleado - herencia común
class Empleado:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self._id_empleado = id_empleado  # Encapsulación
        self._salario_base = 0

