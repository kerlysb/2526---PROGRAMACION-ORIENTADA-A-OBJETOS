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

    def calcular_promedio(self):
        """Calcula promedio semanal"""
        return sum(self.__temperaturas) / len(self.__temperaturas)

# Datos de ejemplo (7 días)
temperaturas_semana = [28.5, 29.2, 27.8, 30.1, 29.5, 31.0, 28.9]
# Uso de la clase
semana_obj = SemanaClima(temperaturas_semana)
semana_obj.mostrar_datos_diarios()
promedio_poo = semana_obj.calcular_promedio()
print(f"Promedio POO: {promedio_poo:.2f}°C")
