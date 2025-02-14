# 👉 Problema: La clase DispositivoMultifuncion obliga a 
# todas sus subclases a implementar funciones que no necesitan.

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
    
# SOLUCIÓN
# from abc import ABC, abstractmethod
    
# class Imprimible():
#     @abstractmethod
#     def imprimir(self):
#         pass
    
# class Escaneble():
#     @abstractmethod
#     def escanear(self):
#         pass
    
# class EnviadoraFax():
#     @abstractmethod
#     def enviar_fax(self):
#         pass
        
    
# class Impresora(Imprimible): 
#     def imprimir(self):
#         print("Imprimiendo documento...")
        
# class Escaner(Escaneble):
#     def escanear(self):
#         print("Escaneando documento...")    
# class Fax(EnviadoraFax):
#     def enviar_fax(self):
#         print("Enviando fax...")    
        
# class ImpresoraConEscaner(Imprimible, Escaneble):       
#     def imprimir(self):
#         print("ImpresoraConEscaner imprimiendo documento...")
#     def escanear(self):
#         print("ImpresoraConEscaner escaneando documento...")  
        
# impresora = Impresora()
# impresora.imprimir()   
# fax = Fax()
# fax.enviar_fax()
# escaner = Escaner()
# escaner.escanear()
# impresoraConEscaner = ImpresoraConEscaner()
# impresoraConEscaner.escanear()
# impresoraConEscaner.imprimir()
        
   
# 🚀 **Desafío:** Refactoriza este código dividiendo la 
# interfaz en responsabilidades más específicas.
# ✅ Pista: Crea interfaces separadas para Imprimir, 
# Escanear y EnviarFax, y haz que las clases implementen 
# solo lo que necesiten.