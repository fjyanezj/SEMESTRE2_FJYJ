import json

class Producto:
    # Clase que representa un producto en el inventario
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Método para actualizar la cantidad del producto
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    # Método para actualizar el precio del producto
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Método para convertir el objeto en un diccionario (para almacenamiento en JSON)
    def to_dict(self):
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

class Inventario:
    # Clase que gestiona el inventario de productos
    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    # Método para agregar un producto al inventario
    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto
        self.guardar_en_archivo()

    # Método para eliminar un producto por su ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()

    # Método para actualizar la cantidad o el precio de un producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_en_archivo()

    # Método para buscar productos por nombre
    def buscar_producto(self, nombre):
        return [p.to_dict() for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    # Método para mostrar todos los productos del inventario
    def mostrar_todos(self):
        return [p.to_dict() for p in self.productos.values()]

    # Método para guardar el inventario en un archivo JSON
    def guardar_en_archivo(self, archivo="inventario.json"):
        with open(archivo, "w") as f:
            json.dump([p.to_dict() for p in self.productos.values()], f, indent=4)

    # Método para cargar el inventario desde un archivo JSON
    def cargar_desde_archivo(self, archivo="inventario.json"):
        try:
            with open(archivo, "r") as f:
                productos = json.load(f)
                self.productos = {p["id"]: Producto(p["id"], p["nombre"], p["cantidad"], p["precio"]) for p in productos}
        except FileNotFoundError:
            self.productos = {}

if __name__ == "__main__":
    inventario = Inventario()
    while True:
        # Menú interactivo para gestionar el inventario
        print("\n1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Agregar un nuevo producto
            id_producto = input("ID del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            # Eliminar un producto por ID
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            # Actualizar la cantidad o el precio de un producto
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no se actualiza): ")
            precio = input("Nuevo precio (dejar vacío si no se actualiza): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            # Buscar productos por nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            print(resultados if resultados else "No se encontraron productos.")

        elif opcion == "5":
            # Mostrar todos los productos en el inventario
            print(inventario.mostrar_todos())

        elif opcion == "6":
            # Salir del programa
            break

        else:
            print("Opción no válida.")
