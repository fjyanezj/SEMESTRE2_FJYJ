class Libro:
    def __init__(self, titulo, autor):
        """
        Constructor: Inicializa los atributos del objeto Libro.
        """
        self.titulo = titulo
        self.autor = autor
        print(f"El libro '{self.titulo}' de {self.autor} ha sido agregado al sistema.")

    def __del__(self):
        """
        Destructor: Realiza limpieza cuando el objeto se elimina.
        """
        print(f"El libro '{self.titulo}' ha sido eliminado del sistema.")

class Biblioteca:
    def __init__(self):
        """
        Constructor: Inicializa la lista de libros disponibles.
        """
        self.libros = []
        print("Se ha inicializado la biblioteca.")

    def agregar_libro(self, titulo, autor):
        """
        Agrega un nuevo libro a la biblioteca.
        """
        libro = Libro(titulo, autor)
        self.libros.append(libro)
        print(f"El libro '{titulo}' ha sido agregado a la colecci�n.")

    def prestar_libro(self, titulo):
        """
        Simula el pr�stamo de un libro si est� disponible.
        """
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                print(f"El libro '{titulo}' ha sido prestado.")
                return
        print(f"El libro '{titulo}' no est� disponible.")

    def devolver_libro(self, titulo, autor):
        """
        Simula la devoluci�n de un libro.
        """
        self.agregar_libro(titulo, autor)
        print(f"El libro '{titulo}' ha sido devuelto.")

    def __del__(self):
        """
        Destructor: Limpia los recursos de la biblioteca al eliminar el objeto.
        """
        print("La biblioteca est� cerrando y todos los recursos han sido liberados.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear la biblioteca
    biblioteca = Biblioteca()

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro("Cien a�os de soledad", "Gabriel Garc�a M�rquez")
    biblioteca.agregar_libro("Don Quijote de la Mancha", "Miguel de Cervantes")

    # Prestar un libro
    biblioteca.prestar_libro("Cien a�os de soledad")

    # Devolver un libro
    biblioteca.devolver_libro("Cien a�os de soledad", "Gabriel Garc�a M�rquez")

    # Finalizar el programa (los destructores se activan autom�ticamente)
