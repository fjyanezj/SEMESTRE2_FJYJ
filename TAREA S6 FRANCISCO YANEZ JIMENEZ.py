# Clase base: Vehículo
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca  # Atributo público
        self.modelo = modelo  # Atributo público
        self.__anio = anio  # Atributo privado (encapsulado)

    # Método para acceder al atributo privado __anio (getter)
    def obtener_anio(self):
        return self.__anio

    # Método para modificar el atributo privado __anio (setter)
    def establecer_anio(self, anio):
        if anio > 1886:  # Validación: El primer automóvil fue fabricado en 1886
            self.__anio = anio
        else:
            print("Año inválido. Debe ser mayor a 1886.")

    # Método general
    def mostrar_info(self):
        return f"Vehículo: {self.marca} {self.modelo}, Año: {self.obtener_anio()}"

# Clase derivada: Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)  # Herencia
        self.num_puertas = num_puertas  # Atributo adicional

    # Sobrescritura de método (Polimorfismo)
    def mostrar_info(self):
        return f"Coche: {self.marca} {self.modelo}, Año: {self.obtener_anio()}, Puertas: {self.num_puertas}"

# Clase derivada: Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo_moto):
        super().__init__(marca, modelo, anio)  # Herencia
        self.tipo_moto = tipo_moto  # Atributo adicional

    # Sobrescritura de método (Polimorfismo)
    def mostrar_info(self):
        return f"Moto: {self.marca} {self.modelo}, Año: {self.obtener_anio()}, Tipo: {self.tipo_moto}"


# Ejecución del programa
if __name__ == "__main__":
    # Crear instancias de las clases
    vehiculo1 = Vehiculo("Genérico", "Modelo X", 2000)
    coche1 = Coche("Toyota", "Corolla", 2015, 4)
    moto1 = Moto("Honda", "CBR", 2020, "Deportiva")

    # Mostrar información
    print(vehiculo1.mostrar_info())
    print(coche1.mostrar_info())
    print(moto1.mostrar_info())

    # Encapsulación: Modificar el año de fabricación
    vehiculo1.establecer_anio(1999)
    print(vehiculo1.mostrar_info())

    # Polimorfismo en acción
    vehiculos = [vehiculo1, coche1, moto1]
    for v in vehiculos:
        print(v.mostrar_info())
