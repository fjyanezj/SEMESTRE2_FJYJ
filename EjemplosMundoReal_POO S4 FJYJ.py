# Sistema de reservas de habitaciones en un hotel

class Habitacion:
    """
    Clase que representa una habitación en un hotel.
    Atributos:
        numero (int): Número de la habitación.
        tipo (str): Tipo de la habitación (Ejemplo: "simple", "doble", "suite").
        precio (float): Precio por noche de la habitación.
        disponible (bool): Estado de disponibilidad de la habitación.
    """
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True  # Todas las habitaciones están disponibles al inicio

    def ocupar(self):
        """Marca la habitación como ocupada."""
        self.disponible = False

    def liberar(self):
        """Marca la habitación como disponible."""
        self.disponible = True

    def __str__(self):
        """Representación en texto de la habitación."""
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación {self.numero}: {self.tipo} - ${self.precio:.2f}/noche ({estado})"


class Hotel:
    """
    Clase que representa un hotel.
    Atributos:
        nombre (str): Nombre del hotel.
        habitaciones (list): Lista de objetos Habitacion disponibles en el hotel.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        """Agrega una habitación al hotel.
        Args:
            habitacion (Habitacion): Objeto de tipo Habitacion.
        """
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        """Muestra todas las habitaciones disponibles en el hotel."""
        print(f"\nHabitaciones disponibles en {self.nombre}:\n")
        for habitacion in self.habitaciones:
            if habitacion.disponible:
                print(habitacion)

    def reservar_habitacion(self, numero):
        """Reserva una habitación según su número.
        Args:
            numero (int): Número de la habitación a reservar.
        """
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                if habitacion.disponible:
                    habitacion.ocupar()
                    print(f"\nLa habitación {numero} ha sido reservada con éxito.")
                else:
                    print(f"\nLa habitación {numero} ya está ocupada.")
                return
        print(f"\nLa habitación {numero} no existe.")

    def liberar_habitacion(self, numero):
        """Libera una habitación según su número.
        Args:
            numero (int): Número de la habitación a liberar.
        """
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                if not habitacion.disponible:
                    habitacion.liberar()
                    print(f"\nLa habitación {numero} ha sido liberada.")
                else:
                    print(f"\nLa habitación {numero} ya está disponible.")
                return
        print(f"\nLa habitación {numero} no existe.")

# --- Ejemplo de uso ---

def main():
    # Crear un hotel
    mi_hotel = Hotel("Hotel Python Paradise")

    # Agregar habitaciones al hotel
    mi_hotel.agregar_habitacion(Habitacion(101, "Simple", 50.0))
    mi_hotel.agregar_habitacion(Habitacion(102, "Doble", 80.0))
    mi_hotel.agregar_habitacion(Habitacion(103, "Suite", 150.0))

    # Mostrar habitaciones disponibles
    mi_hotel.mostrar_habitaciones_disponibles()

    # Reservar una habitación
    mi_hotel.reservar_habitacion(102)

    # Mostrar habitaciones disponibles después de la reserva
    mi_hotel.mostrar_habitaciones_disponibles()

    # Liberar una habitación
    mi_hotel.liberar_habitacion(102)

    # Mostrar habitaciones disponibles después de liberar
    mi_hotel.mostrar_habitaciones_disponibles()

if __name__ == "__main__":
    main()
