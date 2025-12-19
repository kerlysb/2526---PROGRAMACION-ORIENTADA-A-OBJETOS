# Clase base para todos los eventos - demuestra herencia y abstracción
class Evento:
    def __init__(self, nombre, fecha, capacidad_maxima):
        self.nombre = nombre
        self.fecha = fecha
        self.capacidad_maxima = capacidad_maxima
        self.asistentes = []  # Lista de objetos Asistente

    def agregar_asistente(self, asistente):
        """Método para registrar asistentes, controlando capacidad"""
        if len(self.asistentes) < self.capacidad_maxima:
            self.asistentes.append(asistente)
            print(f"Asistente {asistente.nombre} registrado en {self.nombre}")
        else:
            print(f"Evento {self.nombre} está lleno")

    def capacidad_actual(self):
        """Método para consultar ocupación"""
        return len(self.asistentes)

    def descripcion(self):
        """Método abstracto - polimorfismo (se sobrescribe en subclases)"""
        return f"Evento: {self.nombre} - Fecha: {self.fecha}"

    # Clase para asistentes - encapsulación de datos personales
    class Asistente:
        def __init__(self, nombre, email):
            self._nombre = nombre  # Encapsulación con _ (convención privada)
            self._email = email

        @property
        def nombre(self):
            """Getter para nombre - acceso controlado"""
            return self._nombre

        def enviar_confirmacion(self):
            """Método de interacción entre objetos"""
            return f"Confirmación enviada a {self._email}"


# Subclase que hereda de Evento - polimorfismo en descripcion()
class Conferencia(Evento):
    def __init__(self, nombre, fecha, capacidad_maxima, tema):
        super().__init__(nombre, fecha, capacidad_maxima)
        self.tema = tema

    def descripcion(self):
        """Sobrescribe método padre - polimorfismo"""
        return f"Conferencia: {self.nombre} ({self.tema}) - {super().descripcion()}"
