# Sistema de reservas de habitaciones en un hotel

class Habitacion:
    """
    Clase que representa una habitaci�n en un hotel.
    Atributos:
        numero (int): N�mero de la habitaci�n.
        tipo (str): Tipo de la habitaci�n (Ejemplo: "simple", "doble", "suite").
        precio (float): Precio por noche de la habitaci�n.
        disponible (bool): Estado de disponibilidad de la habitaci�n.
    """
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True  # Todas las habitaciones est�n disponibles al inicio

    def ocupar(self):
        """Marca la habitaci�n como ocupada."""
        self.disponible = False

    def liberar(self):
        """Marca la habitaci�n como disponible."""
        self.disponible = True

    def __str__(self):
        """Representaci�n en texto de la habitaci�n."""
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitaci�n {self.numero}: {self.tipo} - ${self.precio:.2f}/noche ({estado})"


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
        """Agrega una habitaci�n al hotel.
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
        """Reserva una habitaci�n seg�n su n�mero.
        Args:
            numero (int): N�mero de la habitaci�n a reservar.
        """
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                if habitacion.disponible:
                    habitacion.ocupar()
                    print(f"\nLa habitaci�n {numero} ha sido reservada con �xito.")
                else:
                    print(f"\nLa habitaci�n {numero} ya est� ocupada.")
                return
        print(f"\nLa habitaci�n {numero} no existe.")

    def liberar_habitacion(self, numero):
        """Libera una habitaci�n seg�n su n�mero.
        Args:
            numero (int): N�mero de la habitaci�n a liberar.
        """
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                if not habitacion.disponible:
                    habitacion.liberar()
                    print(f"\nLa habitaci�n {numero} ha sido liberada.")
                else:
                    print(f"\nLa habitaci�n {numero} ya est� disponible.")
                return
        print(f"\nLa habitaci�n {numero} no existe.")

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

    # Reservar una habitaci�n
    mi_hotel.reservar_habitacion(102)

    # Mostrar habitaciones disponibles despu�s de la reserva
    mi_hotel.mostrar_habitaciones_disponibles()

    # Liberar una habitaci�n
    mi_hotel.liberar_habitacion(102)

    # Mostrar habitaciones disponibles despu�s de liberar
    mi_hotel.mostrar_habitaciones_disponibles()

if __name__ == "__main__":
    main()
