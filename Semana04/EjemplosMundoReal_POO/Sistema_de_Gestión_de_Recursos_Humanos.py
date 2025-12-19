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
        self._salario_base = 500

    def calcular_salario(self):
        """Polimorfismo: salario con bono por lenguaje"""
        bono = 500 if self.lenguaje == "Python" else 200
        return self._salario_base + bono

# Clase Gerente - herencia múltiple simulada con composición
class Gerente(Empleado):
    def __init__(self, nombre, id_empleado, equipo_size):
        super().__init__(nombre, id_empleado)
        self._salario_base = 1500
        self.equipo_size = equipo_size
        self.equipo = []  # Composición: contiene otros Empleados

    def agregar_empleado_equipo(self, empleado):
        """Interacción entre objetos - composición"""
        if len(self.equipo) < self.equipo_size:
            self.equipo.append(empleado)
            print(f"{empleado.nombre} asignado al equipo de {self.nombre}")

    def calcular_salario(self):
        """Polimorfismo: salario con bono por equipo"""
        bono_equipo = len(self.equipo) * 150
        return self._salario_base + bono_equipo
