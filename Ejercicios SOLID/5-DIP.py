# 👉 Problema: La clase Tienda depende directamente de 
# PagoTarjeta, lo que dificulta cambiar de método de pago.

class PagoTarjeta:
    def pagar(self, monto):
        print(f"Pagando {monto} con tarjeta")

class Tienda:
    def __init__(self):
        self.metodo_pago = PagoTarjeta()

    def comprar(self, monto):
        self.metodo_pago.pagar(monto)
        
# SOLUCIÓN

# from abc import ABC, abstractmethod

# class MetodoPago(ABC):
#     @abstractmethod
#     def pagar(self, monto):
#         pass

# class PagoTarjeta(MetodoPago):
#     def pagar(self, monto):
#         print(f"Pagando {monto} con tarjeta")
        
# class PagoPaypal(MetodoPago):
#     def pagar(self, monto):
#         print(f"Pagando {monto} con Paypal")
        
# class PagoEfectivo(MetodoPago):
#     def pagar(self, monto):
#         print(f"Pagando {monto} con efectivo")
        
# class Tienda:
#     def __init__(self, metodo_pago:MetodoPago):
#         self.metodo_pago = metodo_pago

#     def comprar(self, monto):
#         self.metodo_pago.pagar(monto)


# tiendaEfectivo = Tienda(PagoEfectivo())
# tiendaEfectivo.comprar(2000)

# tiendaPaypal = Tienda(PagoPaypal())
# tiendaPaypal.comprar(2000)
# # 🚀 **Desafío:** Refactoriza el código para que 
# `Tienda` no dependa de una implementación específica, 
# sino de una abstracción.
# ✅ Pista: Usa una interfaz o clase base para 
# representar métodos de pago y permite que Tienda 
# reciba diferentes formas de pago.