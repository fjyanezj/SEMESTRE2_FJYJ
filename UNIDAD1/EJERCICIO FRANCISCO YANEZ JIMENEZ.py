# Definici�n de la clase Persona
class Persona:
    # M�todo constructor: se ejecuta cuando se crea un objeto de esta clase
    def __init__(self, nombre, edad):
        # Atributos de la clase (encapsulan datos espec�ficos de cada objeto)
        self.nombre = nombre  # Nombre de la persona
        self.edad = edad      # Edad de la persona

    # M�todo para mostrar informaci�n de la persona
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    # M�todo para actualizar la edad
    def actualizar_edad(self, nueva_edad):
        self.edad = nueva_edad  # Cambia el valor del atributo "edad"
        print(f"La edad de {self.nombre} se ha actualizado a {self.edad}")

# Programa principal
def main():
    # Crear un objeto de la clase Persona
    persona1 = Persona("Carlos", 25)  # Instancia con nombre "Carlos" y edad 25

    # Mostrar informaci�n inicial
    print("Informaci�n inicial:")
    persona1.mostrar_informacion()

    # Actualizar la edad de la persona
    print("\nActualizando la edad...")
    persona1.actualizar_edad(30)

    # Mostrar informaci�n actualizada
    print("\nInformaci�n actualizada:")
    persona1.mostrar_informacion()

# Llamada al programa principal
if __name__ == "__main__":
    main()
