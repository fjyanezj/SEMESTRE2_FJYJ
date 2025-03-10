class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.info = (titulo, autor)  # Tupla para datos inmutables

class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista para almacenar libros prestados

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario: ISBN -> Objeto Libro
        self.usuarios = {}  # Diccionario: ID de usuario -> Objeto Usuario
        self.ids_usuarios = set()  # Conjunto para IDs únicos

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print("Libro eliminado exitosamente.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, nombre, user_id):
        if user_id in self.ids_usuarios:
            print("Este ID de usuario ya está registrado.")
        else:
            usuario = Usuario(nombre, user_id)
            self.usuarios[user_id] = usuario
            self.ids_usuarios.add(user_id)
            print(f"Usuario '{nombre}' registrado exitosamente.")

    def dar_de_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.ids_usuarios.remove(user_id)
            print("Usuario eliminado correctamente.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            self.usuarios[user_id].libros_prestados.append(libro)
            print(f"Libro '{libro.titulo}' prestado a {self.usuarios[user_id].nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro '{libro.titulo}' devuelto a la biblioteca.")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        resultados = [libro for libro in self.libros_disponibles.values()
                      if getattr(libro, criterio, None) == valor]
        if resultados:
            for libro in resultados:
                print(f"{libro.titulo} - {libro.autor} ({libro.categoria})")
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(f"{libro.titulo} - {libro.autor}")
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")

# Prueba del sistema
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("1984", "George Orwell", "Ficción", "1234567890")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo Mágico", "0987654321")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
biblioteca.registrar_usuario("Juan Perez", "U001")
biblioteca.registrar_usuario("Maria López", "U002")

# Prestar libro
biblioteca.prestar_libro("U001", "1234567890")

# Listar libros prestados
biblioteca.listar_libros_prestados("U001")

# Devolver libro
biblioteca.devolver_libro("U001", "1234567890")

# Buscar libro
biblioteca.buscar_libro("categoria", "Realismo Mágico")
