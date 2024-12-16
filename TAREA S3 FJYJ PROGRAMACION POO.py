class ClimaSemanal:
    def __init__(self):
        # Encapsulamos los datos de las temperaturas
        self.__temperaturas = []

    # M�todo para ingresar temperaturas
    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura para el d�a {i + 1}: "))
            self.__temperaturas.append(temp)

    # M�todo para calcular el promedio semanal
    def calcular_promedio(self):
        total = sum(self.__temperaturas)
        promedio = total / len(self.__temperaturas)
        return promedio

# Programa principal
def main():
    print("Programa para calcular el promedio semanal del clima (Programaci�n Orientada a Objetos)")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}�C")

# Llamada al programa principal
if __name__ == "__main__":
    main()
