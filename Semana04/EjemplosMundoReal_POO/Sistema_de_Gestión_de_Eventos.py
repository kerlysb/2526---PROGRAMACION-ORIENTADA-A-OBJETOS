# Clase base para todos los eventos - demuestra herencia y abstracción
class Evento:
    def __init__(self, nombre, fecha, capacidad_maxima):
        self.nombre = nombre
        self.fecha = fecha
        self.capacidad_maxima = capacidad_maxima
        self.asistentes = []  # Lista de objetos Asistente