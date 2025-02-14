# 👉 Problema: La clase Reporte maneja tanto la 
# generación del contenido como la impresión.
# Se debe dividir la responsabilidad en clases separadas.
class Reporte:
    def __init__(self, contenido):
        self.contenido = contenido

    def generar_pdf(self):
        print(f"Generando PDF con contenido: {self.contenido}")
        
    
# SOLUCIÓN

# class Reporte:
#     def __init__(self, contenido):
#         self.contenido = contenido

# class GeneradorPDF:
#     def generar(self, reporte: Reporte):
#         print(f"Generando PDF con contenido: {reporte.contenido}")

# reporte = Reporte("Informe de recursos humanos")
# generador = GeneradorPDF()
# generador.generar(reporte)


# 🚀 **Desafío:** Refactoriza este código para 
# que cada clase tenga una única responsabilidad.
# ✅ Pista: Crea una clase para el contenido y otra 
# para la generación del PDF.