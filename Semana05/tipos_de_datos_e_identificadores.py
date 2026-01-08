"""
Programa para calcular el área de un rectángulo.
"""

def calcular_area(largo: float, ancho: float) -> float:
    """
    Calcula el área de un rectángulo.

    Args:
        largo (float): Largo del rectángulo en metros.
        ancho (float): Ancho del rectángulo en metros.

    Returns:
        float: Área calculada.
    """
# Validación booleana para dimensiones positivas
    dimensiones_validas = largo > 0 and ancho > 0
    if not dimensiones_validas:
        print("Error: Las dimensiones deben ser positivas.")
        return 0.0

   # Cálculo del área (float)
    area_rectangulo = largo * ancho
    return area_rectangulo

# Datos de entrada (tipos mixtos)
largo_rectangulo = 10  # int
ancho_rectangulo = 5.5  # float
nombre_figura = "rectángulo principal"  # str
calcular_area_automatico = True  # bool



