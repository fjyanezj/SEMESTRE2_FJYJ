# Definición de la clase Persona
class Persona:
    # Método constructor: se ejecuta cuando se crea un objeto de esta clase
    def __init__(self, nombre, edad):
        # Atributos de la clase (encapsulan datos específicos de cada objeto)
        self.nombre = nombre  # Nombre de la persona
        self.edad = edad      # Edad de la persona

    # Método para mostrar información de la persona
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    # Método para actualizar la edad
    def actualizar_edad(self, nueva_edad):
        self.edad = nueva_edad  # Cambia el valor del atributo "edad"
        print(f"La edad de {self.nombre} se ha actualizado a {self.edad}")

# Programa principal
def main():
    # Crear un objeto de la clase Persona
    persona1 = Persona("Carlos", 25)  # Instancia con nombre "Carlos" y edad 25

    # Mostrar información inicial
    print("Información inicial:")
    persona1.mostrar_informacion()

    # Actualizar la edad de la persona
    print("\nActualizando la edad...")
    persona1.actualizar_edad(30)

    # Mostrar información actualizada
    print("\nInformación actualizada:")
    persona1.mostrar_informacion()

# Llamada al programa principal
if __name__ == "__main__":
    main()
