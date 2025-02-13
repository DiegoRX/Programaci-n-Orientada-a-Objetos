# 👉 Problema: La clase Reporte maneja tanto la 
# generación del contenido como la impresión.
# Se debe dividir la responsabilidad en clases separadas.
class Reporte:
    def __init__(self, contenido):
        self.contenido = contenido

    def generar_pdf(self):
        print(f"Generando PDF con contenido: {self.contenido}")

# 🚀 **Desafío:** Refactoriza este código para 
# que cada clase tenga una única responsabilidad.
# ✅ Pista: Crea una clase para el contenido y otra 
# para la generación del PDF.