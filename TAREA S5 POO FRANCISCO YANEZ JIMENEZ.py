"""
Programa para calcular el �rea de un tri�ngulo.
Autor: FRANCISCO YANEZ JIMENEZ
"""

def calcular_area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el �rea de un tri�ngulo dado su base y altura.
    Retorna:
        - �rea del tri�ngulo si los valores son v�lidos.
        - -1 si hay un error en los datos de entrada.
    """
    if base <= 0 or altura <= 0:
        print("Error: Base y altura deben ser positivos.")
        return -1

    return (base * altura) / 2

if __name__ == "__main__":
    print("Calculadora de �rea de tri�ngulos")
    try:
        base_triangulo: float = float(input("Base: "))
        altura_triangulo: float = float(input("Altura: "))

        area_calculada: float = calcular_area_triangulo(base_triangulo, altura_triangulo)

        if area_calculada != -1:
            print(f"�rea: {area_calculada:.2f}")
        else:
            print("No se pudo calcular el �rea debido a un error en los datos de entrada.")

        nombre_figura: str = "Tri�ngulo"
        print(f"Figura: {nombre_figura}")

    except ValueError:
        print("Error: Por favor, ingrese valores num�ricos v�lidos para la base y la altura.")
