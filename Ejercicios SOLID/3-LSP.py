# 🟡 Ejercicio 3: Principio de Sustitución de Liskov (LSP)
# 👉 Problema: Se tiene una clase base Vehiculo y 
# una subclase Bicicleta. Sin embargo, la subclase 
# sobrescribe un método de forma inapropiada.

class Vehiculo:
    def encender(self):
        print("El vehículo está en marcha")

class Bicicleta(Vehiculo):
    def encender(self):
        raise Exception("¡Una bicicleta no se enciende!")
    
# # SOLUCIÓN

# from abc import ABC, abstractmethod

# class Vehiculo(ABC):
#     @abstractmethod
#     def mover():
#         pass
    
# class VehiculoMotorizado(Vehiculo):
#     def mover(self):
#         pass
        
# class VehiculoNoMotorizado(Vehiculo):
#     def mover(self):
#         pass
    
# class Carro(VehiculoMotorizado):
#     def mover(self):
#         print("Carro enciende y está en marcha")
    
# class Moto(VehiculoMotorizado):
#     def mover(self):
#         print("Moto enciende y está en marcha")
    
# class Bicicleta(VehiculoNoMotorizado):
#     def mover(self):
#         print("La bicicleta avanza al pedalear")    
        
# class Skate(VehiculoNoMotorizado):
#     def mover(self):
#         print("El skate avanza.") 
        
# vehiculos = [Carro(), Moto(), Bicicleta(), Skate()]
# for vehiculo in vehiculos:
#     vehiculo.mover()
    

# 🚀 **Desafío:** Refactoriza este código para que 
# las subclases puedan sustituir a la clase base 
# sin generar errores inesperados.
# ✅ Pista: Reestructura la jerarquía de clases 
# para que solo los vehículos motorizados hereden 
# el método arrancar.

