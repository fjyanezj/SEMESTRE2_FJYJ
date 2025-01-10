"""
Programa para calcular el área de un triángulo.
Autor: FRANCISCO YANEZ JIMENEZ
"""

def calcular_area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un triángulo dado su base y altura.
    Retorna:
        - Área del triángulo si los valores son válidos.
        - -1 si hay un error en los datos de entrada.
    """
    if base <= 0 or altura <= 0:
        print("Error: Base y altura deben ser positivos.")
        return -1

    return (base * altura) / 2

if __name__ == "__main__":
    print("Calculadora de área de triángulos")
    try:
        base_triangulo: float = float(input("Base: "))
        altura_triangulo: float = float(input("Altura: "))

        area_calculada: float = calcular_area_triangulo(base_triangulo, altura_triangulo)

        if area_calculada != -1:
            print(f"Área: {area_calculada:.2f}")
        else:
            print("No se pudo calcular el área debido a un error en los datos de entrada.")

        nombre_figura: str = "Triángulo"
        print(f"Figura: {nombre_figura}")

    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos para la base y la altura.")
