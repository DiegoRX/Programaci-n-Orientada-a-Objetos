# 👉 Problema: La clase DispositivoMultifuncion obliga a todas sus subclases a implementar funciones que no necesitan.

class DispositivoMultifuncion:
    def imprimir(self):
        pass

    def escanear(self):
        pass

    def enviar_fax(self):
        pass

class Impresora(DispositivoMultifuncion):
    def imprimir(self):
        print("Imprimiendo documento...")

    def escanear(self):
        raise Exception("¡Una impresora no puede escanear!")

    def enviar_fax(self):
        raise Exception("¡Una impresora no puede enviar fax!")

# 🚀 **Desafío:** Refactoriza este código dividiendo la interfaz en responsabilidades más específicas.
# ✅ Pista: Crea interfaces separadas para Imprimir, Escanear y EnviarFax, y haz que las clases implementen solo lo que necesiten.