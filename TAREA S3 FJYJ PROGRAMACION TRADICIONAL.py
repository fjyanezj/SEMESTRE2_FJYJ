def ingresar_datos_diarios():

    """
    Pide al usuario que ingrese las temperaturas diarias de una semana.
    Retorna una lista con las temperaturas ingresadas.
    """
    temperaturas = []

    for dia in range(1, 8):

        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))

        temperaturas.append(temperatura)


    return temperaturas



def calcular_promedio(temperaturas):

    """
    Calcula el promedio de una lista de temperaturas.
    """

    suma = sum(temperaturas)

    promedio = suma / len(temperaturas)

    return promedio



# Obtener las temperaturas diarias

temperaturas = ingresar_datos_diarios()

# Calcular el promedio semanal

promedio_semanal = calcular_promedio(temperaturas)



# Mostrar el resultado

print(f"El promedio semanal de temperatura es: {promedio_semanal:.2f} °C")