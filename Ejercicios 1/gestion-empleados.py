class Empleado:
    def __init__(self, nombre, edad, salario_base):
        self.nombre = nombre
        self.edad = edad
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base


class EmpleadoFijo(Empleado):
    def __init__(self, nombre, edad, salario_base, bono):
        super().__init__(nombre, edad, salario_base)
        self.bono = bono

    def calcular_salario(self):
        return self.salario_base + self.bono


class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, edad, salario_base, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, edad, salario_base)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora


def calcular_salario_total(empleados):
    total = 0
    for empleado in empleados:
        total += empleado.calcular_salario()
        print(f"Salario de {empleado.nombre}: {empleado.calcular_salario()}")
    print(f"Total de salarios: {total}")


# Ejemplo de uso
empleados = [
    EmpleadoFijo("Juan", 30, 2000, 500),
    EmpleadoPorHora("Ana", 25, 0, 160, 15),
    EmpleadoFijo("Carlos", 40, 2500, 700)
]

calcular_salario_total(empleados)