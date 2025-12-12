# Programación Orientada a Objetos (POO)
class SemanaClima:
    """Clase para gestionar datos climáticos semanales"""
    def __init__(self, temperaturas):
        self.__temperaturas = temperaturas  # Encapsulamiento
        self.dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

        def mostrar_datos_diarios(self):
            """Muestra temperaturas por día"""
            for i, dia in enumerate(self.dias):
                print(f"{dia}: {self.__temperaturas[i]:.1f}°C")