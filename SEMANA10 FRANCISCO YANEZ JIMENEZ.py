import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def to_line(self):
        """Convierte el producto en una línea de texto para guardar en el archivo."""
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def from_line(line):
        """Convierte una línea de texto en un objeto Producto."""
        try:
            id, nombre, cantidad, precio = line.strip().split(',')
            return Producto(int(id), nombre, int(cantidad), float(precio))
        except ValueError:
            print(f"Error al leer la línea: {line}")
            return None

class Inventario:
    FILE_NAME = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo al iniciar el programa."""
        if not os.path.exists(self.FILE_NAME):
            open(self.FILE_NAME, 'w').close()  # Crea el archivo si no existe

        try:
            with open(self.FILE_NAME, 'r') as file:
                for line in file:
                    producto = Producto.from_line(line)
                    if producto:
                        self.productos.append(producto)
            print("Inventario cargado correctamente.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda todos los productos en el archivo de texto."""
        try:
            with open(self.FILE_NAME, 'w') as file:
                for producto in self.productos:
                    file.write(producto.to_line())
            print("Inventario guardado correctamente.")
        except PermissionError:
            print("Error: No tienes permiso para escribir en el archivo.")

    def añadir_producto(self, producto):
        """Añade un nuevo producto y guarda en el archivo."""
        if any(p.id == producto.id for p in self.productos):
            print("Error: El ID ya existe.")
            return
        self.productos.append(producto)
        self.guardar_inventario()
        print(f"Producto {producto.nombre} añadido correctamente.")

    def eliminar_producto(self, id):
        """Elimina un producto y guarda los cambios en el archivo."""
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                self.guardar_inventario()
                print(f"Producto {producto.nombre} eliminado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """Actualiza la cantidad o precio de un producto y guarda los cambios."""
        for producto in self.productos:
            if producto.id == id:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_inventario()
                print(f"Producto {producto.nombre} actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre (puede haber coincidencias parciales)."""
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if self.productos:
            for p in self.productos:
                print(p)
        else:
            print("El inventario está vacío.")

def mostrar_menu():
    print("\nSistema de Gestión de Inventarios")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def interfaz_usuario():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            try:
                id = int(input("Introduce el ID del producto: "))
                nombre = input("Introduce el nombre del producto: ")
                cantidad = int(input("Introduce la cantidad: "))
                precio = float(input("Introduce el precio: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Entrada inválida. Asegúrate de ingresar números válidos.")

        elif opcion == '2':
            try:
                id = int(input("Introduce el ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print("Error: El ID debe ser un número entero.")

        elif opcion == '3':
            try:
                id = int(input("Introduce el ID del producto a actualizar: "))
                cantidad = input("Introduce la nueva cantidad (deja en blanco para no cambiar): ")
                precio = input("Introduce el nuevo precio (deja en blanco para no cambiar): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id, cantidad, precio)
            except ValueError:
                print("Error: Asegúrate de ingresar valores numéricos válidos.")

        elif opcion == '4':
            nombre = input("Introduce el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    interfaz_usuario()
