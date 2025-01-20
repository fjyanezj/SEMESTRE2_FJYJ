# Clase base: Veh�culo
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca  # Atributo p�blico
        self.modelo = modelo  # Atributo p�blico
        self.__anio = anio  # Atributo privado (encapsulado)

    # M�todo para acceder al atributo privado __anio (getter)
    def obtener_anio(self):
        return self.__anio

    # M�todo para modificar el atributo privado __anio (setter)
    def establecer_anio(self, anio):
        if anio > 1886:  # Validaci�n: El primer autom�vil fue fabricado en 1886
            self.__anio = anio
        else:
            print("A�o inv�lido. Debe ser mayor a 1886.")

    # M�todo general
    def mostrar_info(self):
        return f"Veh�culo: {self.marca} {self.modelo}, A�o: {self.obtener_anio()}"

# Clase derivada: Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)  # Herencia
        self.num_puertas = num_puertas  # Atributo adicional

    # Sobrescritura de m�todo (Polimorfismo)
    def mostrar_info(self):
        return f"Coche: {self.marca} {self.modelo}, A�o: {self.obtener_anio()}, Puertas: {self.num_puertas}"

# Clase derivada: Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo_moto):
        super().__init__(marca, modelo, anio)  # Herencia
        self.tipo_moto = tipo_moto  # Atributo adicional

    # Sobrescritura de m�todo (Polimorfismo)
    def mostrar_info(self):
        return f"Moto: {self.marca} {self.modelo}, A�o: {self.obtener_anio()}, Tipo: {self.tipo_moto}"


# Ejecuci�n del programa
if __name__ == "__main__":
    # Crear instancias de las clases
    vehiculo1 = Vehiculo("Gen�rico", "Modelo X", 2000)
    coche1 = Coche("Toyota", "Corolla", 2015, 4)
    moto1 = Moto("Honda", "CBR", 2020, "Deportiva")

    # Mostrar informaci�n
    print(vehiculo1.mostrar_info())
    print(coche1.mostrar_info())
    print(moto1.mostrar_info())

    # Encapsulaci�n: Modificar el a�o de fabricaci�n
    vehiculo1.establecer_anio(1999)
    print(vehiculo1.mostrar_info())

    # Polimorfismo en acci�n
    vehiculos = [vehiculo1, coche1, moto1]
    for v in vehiculos:
        print(v.mostrar_info())
