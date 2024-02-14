class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def obtener_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"


class Carro(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def obtener_info(self):
        return f"Carro - {super().obtener_info()}, Color: {self.color}"


class Barco(Vehiculo):
    def __init__(self, marca, modelo, eslora):
        super().__init__(marca, modelo)
        self.eslora = eslora

    def obtener_info(self):
        return f"Barco - {super().obtener_info()}, Eslora: {self.eslora} metros"


class Avion(Vehiculo):
    def __init__(self, marca, modelo, capacidad_pasajeros):
        super().__init__(marca, modelo)
        self.capacidad_pasajeros = capacidad_pasajeros

    def obtener_info(self):
        return f"Avión - {super().obtener_info()}, Capacidad de pasajeros: {self.capacidad_pasajeros}"


# Crear objetos de cada tipo de vehículo
mi_carro = Carro(marca="Toyota", modelo="Corolla", color="Azul")
mi_barco = Barco(marca="Yamaha", modelo="123", eslora=10.5)
mi_avion = Avion(marca="Boeing", modelo="747", capacidad_pasajeros=400)

# Imprimir información de los vehículos
print(mi_carro.obtener_info())
print(mi_barco.obtener_info())
print(mi_avion.obtener_info())
