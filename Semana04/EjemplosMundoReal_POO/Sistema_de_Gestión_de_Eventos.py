# Sistema de Gestión de Eventos - VERSIÓN CORREGIDA

# 1. PRIMERO: Clase para asistentes (encapsulación)
class Asistente:
    def __init__(self, nombre, email):
        self._nombre = nombre  # Convención privada
        self._email = email

    @property
    def nombre(self):
        """Getter controlado para nombre"""
        return self._nombre

    def enviar_confirmacion(self):
        """Método de interacción"""
        return f"Confirmación enviada a {self._email}"


# 2. SEGUNDO: Clase base para eventos (herencia y abstracción)
class Evento:
    def __init__(self, nombre, fecha, capacidad_maxima):
        self.nombre = nombre
        self.fecha = fecha
        self.capacidad_maxima = capacidad_maxima
        self.asistentes = []  # Lista de objetos Asistente

    def agregar_asistente(self, asistente):
        """Controla capacidad máxima"""
        if len(self.asistentes) < self.capacidad_maxima:
            self.asistentes.append(asistente)
            print(f"✅ Asistente {asistente.nombre} registrado en {self.nombre}")
        else:
            print(f"❌ Evento {self.nombre} está lleno")

    def capacidad_actual(self):
        """Consulta ocupación actual"""
        return len(self.asistentes)

    def descripcion(self):
        """Método base para polimorfismo"""
        return f"Evento: {self.nombre} - Fecha: {self.fecha}"


# 3. TERCERO: Subclase con polimorfismo
class Conferencia(Evento):
    def __init__(self, nombre, fecha, capacidad_maxima, tema):
        super().__init__(nombre, fecha, capacidad_maxima)
        self.tema = tema

    def descripcion(self):
        """Sobrescribe método padre - POLIMORFISMO"""
        return f"🎤 Conferencia: {self.nombre} ({self.tema}) - {super().descripcion()}"


# 4. ÚLTIMO: Bloque principal (DESPUÉS de todas las clases)
if __name__ == "__main__":
    print("=== SISTEMA DE GESTIÓN DE EVENTOS ===\n")

    # Crear objetos (AHORA las clases existen)
    conf_python = Conferencia("Poo Vs Programación Tradicional", "2025-12-20", 50, "OOP")
    asist1 = Asistente("Kerly Suárez", "kerly_sb@gmail.com")
    asist2 = Asistente("Arturo Acosta", "maria@gmail.com")

    # Interacción entre objetos
    conf_python.agregar_asistente(asist1)
    conf_python.agregar_asistente(asist2)

    print("\n" + conf_python.descripcion())  # Polimorfismo en acción
    print(f" Capacidad: {conf_python.capacidad_actual()}/{conf_python.capacidad_maxima}")
    print(asist1.enviar_confirmacion())
