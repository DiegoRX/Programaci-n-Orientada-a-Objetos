# 👉 Problema: La clase ProcesadorPago se modifica cada vez que se agrega un nuevo método de pago. Debe estar abierta para extensión, pero cerrada para modificación.
class ProcesadorPago:
    def procesar(self, metodo, monto):
        if metodo == "tarjeta":
            print(f"Pagando {monto} con tarjeta")
        elif metodo == "paypal":
            print(f"Pagando {monto} con PayPal")
        else:
            print("Método de pago no soportado")

# 🚀 **Desafío:** Refactoriza este código usando clases para que sea fácil añadir nuevos métodos de pago sin modificar el código existente.
# ✅ Pista: Usa clases separadas para cada método de pago y polimorfismo.

