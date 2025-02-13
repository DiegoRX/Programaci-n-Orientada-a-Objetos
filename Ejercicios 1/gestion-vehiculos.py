class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} ha sido encendido.")
        else:
            print(f"{self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} ha sido apagado.")
        else:
            print(f"{self.marca} {self.modelo} ya está apagado.")

    def moverse(self):
        raise NotImplementedError("Este método debe ser implementado por las clases hijas.")


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, combustible):
        super().__init__(marca, modelo)
        self.combustible = combustible

    def moverse(self):
        if self.encendido:
            if self.combustible > 0:
                self.combustible -= 10
                print(f"{self.marca} {self.modelo} se está moviendo. Combustible restante: {self.combustible}")
            else:
                print(f"{self.marca} {self.modelo} no tiene suficiente combustible para moverse.")
        else:
            print(f"{self.marca} {self.modelo} no puede moverse porque está apagado.")

            
class Avion(Vehiculo):
    def __init__(self, marca, modelo, altura):
        super().__init__(marca, modelo)
        self.altura = altura

    def moverse(self):
        if self.encendido:
               print(f"{self.marca} {self.modelo} está volando a la altura {self.altura} metros.")         
        else:
            print(f"{self.marca} {self.modelo} no puede volar porque está apagado.")
            
    def apagar(self):
        print(f"{self.marca} {self.modelo} ha aterrizado y se ha apagado.")


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def encender(self):
        print(f"{self.marca} {self.modelo} no tiene motor para encender.")

    def apagar(self):
        print(f"{self.marca} {self.modelo} no tiene motor para apagar.")

    def moverse(self):
        print(f"{self.marca} {self.modelo} está pedaleando.")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima):
        super().__init__(marca, modelo)
        self.velocidad_maxima = velocidad_maxima

    def moverse(self):
        if self.encendido:
            print(f"{self.marca} {self.modelo} está acelerando hasta {self.velocidad_maxima} km/h.")
        else:
            print(f"{self.marca} {self.modelo} no puede moverse porque está apagado.")


def simular_movimiento(vehiculos):
    for vehiculo in vehiculos:
        print(f"\n--- Simulando {vehiculo.marca} {vehiculo.modelo} ---")
        vehiculo.encender()
        vehiculo.moverse()
        vehiculo.apagar()


# Ejemplo de uso
vehiculos = [
    Automovil("Toyota", "Corolla", 50),
    Bicicleta("Trek", "Mountain Bike"),
    Motocicleta("Harley-Davidson", "Street 750", 120),
    Avion("Boening","747", 10000)
]

simular_movimiento(vehiculos)