# 1) Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
# titular y cantidad (puede tener decimales).

# El titular será obligatorio y la cantidad es opcional. 
# Crea dos constructores que cumpla lo anterior.

# Crea sus métodos get, set y toString.

# Tendrá dos métodos especiales:

# ingresar( cantidad): se ingresa una cantidad a la cuenta, 
# si la cantidad introducida es negativa, no se hará nada.
# retirar( cantidad): se retira una cantidad a la cuenta, 
# si restando la cantidad actual a la que nos pasan es negativa, 
# la cantidad de la cuenta pasa a ser 0.

#SOLUCIÓN

class Cuenta:
    def __init__(self, titular, cantidad = 0.0):
        self.titular = titular
        self.cantidad = cantidad
        
    def get_titular(self):
        print (f"Titular: {self.titular}" )
        
    def get_cantidad(self):
         print (f"cantidad: {self.cantidad}" )
        
    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.cantidad = cantidad
    # ingresar( cantidad): se ingresa una cantidad a la cuenta, 
# si la cantidad introducida es negativa, no se hará nada.        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        
# retirar( cantidad): se retira una cantidad a la cuenta, 
# si restando la cantidad actual a la que nos pasan es negativa, 
# la cantidad de la cuenta pasa a ser 0.        
    def retirar(self, cantidad):
       self.cantidad -= cantidad
       if self.cantidad < 0:
           self.cantidad = 0
           
    def __str__(self):
        return f"Titular: {self.titular}, balance: {self.cantidad:.2f} "      
           
           
cuentaPedro = Cuenta("Pedro",0)
print(cuentaPedro)

cuentaPedro.ingresar(2000)
print(cuentaPedro)

cuentaPedro.retirar(1000)
print(cuentaPedro)

# cuentaPedro.retirar(5000)
# print(cuentaPedro)

cuentaPedro.ingresar(-2000)
print(cuentaPedro)

cuentaPedro.get_titular()
cuentaPedro.get_cantidad()