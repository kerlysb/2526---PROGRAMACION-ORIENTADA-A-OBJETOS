# Programación Orientada a Objetos (POO)
class SemanaClima:
    """Clase para gestionar datos climáticos semanales"""
    def __init__(self, temperaturas):
        self.__temperaturas = temperaturas  # Encapsulamiento
        self.dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]