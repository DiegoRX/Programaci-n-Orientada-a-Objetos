# 👉 Problema: La clase ProcesadorPago se modifica cada vez 
# que se agrega un nuevo método de pago. 
# Debe estar abierta para extensión, pero cerrada para modificación.
class ProcesadorPago:
    def procesar(self, metodo, monto):
        if metodo == "tarjeta":
            print(f"Pagando {monto} con tarjeta")
        elif metodo == "paypal":
            print(f"Pagando {monto} con PayPal")
        else:
            print("Método de pago no soportado")  
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
        
# class ProcesadorPago():
#     def procesar(self, metodo_pago:MetodoPago,monto):
#         metodo_pago.pagar(monto)
        
# procesador = ProcesadorPago()
# procesador.procesar(PagoEfectivo(), 100)
# procesador.procesar(PagoPaypal(), 200)
# procesador.procesar(PagoTarjeta(), 180)

# 🚀 **Desafío:** Refactoriza este código usando clases para que sea 
# fácil añadir nuevos métodos de pago sin modificar el código existente.
# ✅ Pista: Usa clases separadas para cada método de pago y polimorfismo.

