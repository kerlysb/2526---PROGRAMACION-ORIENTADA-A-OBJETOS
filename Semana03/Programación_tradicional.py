# Programación Tradicional - Promedio semanal del clima
def procesar_temperaturas_diarias(temperaturas):
    """Procesa lista de 7 temperaturas diarias"""
    return temperaturas
def calcular_promedio_semanal(temperaturas):
    """Calcula promedio de temperaturas semanales"""
    return sum(temperaturas) / len(temperaturas)
# Datos de ejemplo (7 días)
temperaturas_semana = [28.5, 29.2, 27.8, 30.1, 29.5, 31.0, 28.9]
temps = procesar_temperaturas_diarias(temperaturas_semana)
promedio_trad = calcular_promedio_semanal(temps)
print(f"Promedio tradicional: {promedio_trad:.2f}°C")