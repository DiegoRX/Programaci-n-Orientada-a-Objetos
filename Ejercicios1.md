# Proyectos de Programación Orientada a Objetos en Python

Este repositorio contiene dos proyectos prácticos desarrollados en Python para practicar conceptos fundamentales de la **Programación Orientada a Objetos (POO)**, como **herencia** y **polimorfismo**. Los proyectos son:

- **Gestión de Vehículos**: Un sistema para modelar diferentes tipos de vehículos y simular su comportamiento.
- **Gestión de Empleados**: Un sistema para calcular salarios de empleados con diferentes tipos de contratos.

---

## Índice
1. [Proyecto 1: Gestión de Vehículos](#proyecto-1-gestión-de-vehículos)
   - Descripción
   - Requisitos
   - Estructura del Código
   - Ejecución
2. [Proyecto 2: Gestión de Empleados](#proyecto-2-gestión-de-empleados)
   - Descripción
   - Requisitos
   - Estructura del Código
   - Ejecución

---

## Proyecto 1: Gestión de Vehículos

### **Descripción**
El proyecto consiste en un sistema para modelar diferentes tipos de vehículos (automóviles, bicicletas, motocicletas) y simular su comportamiento. Cada vehículo tiene métodos para encender/apagar el motor y moverse, con comportamientos específicos según el tipo de vehículo.

### **Requisitos**
- Python 3.x instalado en tu sistema.
- Conocimientos básicos de programación orientada a objetos en Python.

### **Estructura del Código**
El código está organizado en una jerarquía de clases:
1. **Clase Base (`Vehiculo`)**:
   - Contiene atributos comunes (`marca`, `modelo`) y métodos básicos (`encender`, `apagar`, `moverse`).
2. **Clases Hijas**:
   - `Automovil`: Representa un automóvil con combustible.
   - `Bicicleta`: Representa una bicicleta sin motor.
   - `Motocicleta`: Representa una motocicleta con velocidad máxima.

### **Ejecución**
1. Clona este repositorio o copia el código del archivo `gestion_vehiculos.py`.
2. Ejecuta el script en tu terminal:
   ```bash
   python gestion_vehiculos.py
   ```
3. Observa la salida en la consola, que simula el comportamiento de los vehículos.

---

## Proyecto 2: Gestión de Empleados

### **Descripción**
El proyecto consiste en un sistema para calcular los salarios de empleados con diferentes tipos de contratos. Se implementa una jerarquía de clases para representar empleados fijos y empleados por hora, y se utiliza polimorfismo para calcular sus salarios.

### **Requisitos**
- Python 3.x instalado en tu sistema.
- Conocimientos básicos de programación orientada a objetos en Python.

### **Estructura del Código**
El código está organizado en una jerarquía de clases:
1. **Clase Base (`Empleado`)**:
   - Contiene atributos comunes (`nombre`, `edad`, `salario_base`) y un método básico (`calcular_salario`).
2. **Clases Hijas**:
   - `EmpleadoFijo`: Representa un empleado con salario fijo más bono.
   - `EmpleadoPorHora`: Representa un empleado que gana según las horas trabajadas.

### **Ejecución**
1. Clona este repositorio o copia el código del archivo `gestion_empleados.py`.
2. Ejecuta el script en tu terminal:
   ```bash
   python gestion_empleados.py
   ```
3. Observa la salida en la consola, que muestra el salario de cada empleado y el total de salarios.

---

## Instrucciones Generales

### **Instalación**
Asegúrate de tener Python instalado en tu sistema. Puedes verificarlo ejecutando:
```bash
python --version
```
Si no tienes Python instalado, descárgalo desde [python.org](https://www.python.org/downloads/).

### **Ejecutar los Proyectos**
Cada proyecto está contenido en un archivo separado:
- `gestion_vehiculos.py`: Para el proyecto de gestión de vehículos.
- `gestion_empleados.py`: Para el proyecto de gestión de empleados.

Simplemente ejecuta el archivo correspondiente en tu terminal:
```bash
python nombre_del_archivo.py
```


```markdown
# Tareas Adicionales

## Tarea 1: Cálculo del Promedio de Edad de los Empleados

El estudiante debe crear una nueva función que tome las edades de los empleados y calcule la edad promedio. Esta tarea tiene como objetivo practicar el manejo de listas, objetos y métodos en Python.

### Descripción de la Tarea:

**Objetivo:** Crear una función que calcule el promedio de edad de una lista de empleados.

**Requisitos:**
- La función debe recibir una lista de objetos de tipo `Empleado`.
- Debe calcular el promedio de las edades de los empleados utilizando un bucle o una comprensión de lista.
- Si la lista está vacía, la función debe devolver `0` para evitar errores.

**Salida Esperada:**
```
Promedio de edad de los empleados: 31.67
```

---

## Tarea 2: Creación de la Clase `Avion`

El estudiante debe crear una nueva clase llamada `Avion` que modele un vehículo con las siguientes características:
- El avión puede encenderse.
- El avión puede volar a una altura específica.
- El avión puede aterrizar y apagarse.

### Descripción de la Tarea:

**Objetivo:** Practicar la creación de una clase con atributos y métodos que representen un objeto del mundo real.

**Requisitos:**
- La clase debe llamarse `Avion`.
- Debe tener un atributo `encendido` (booleano) para indicar si el avión está encendido o apagado.
- Debe tener un atributo `altura` (numérico) para indicar la altura actual del avión.
- **Métodos requeridos:**
  - `encender()`: Enciende el avión si está apagado.
  - `volar(altura)`: Hace que el avión vuele a una altura específica si está encendido.
  - `aterrizar()`: Hace que el avión aterrice y se apague.
- Validar que el avión no pueda volar si está apagado.

**Salida Esperada:**
```
El avión ha sido encendido.
El avión está volando a una altura de 10000 metros.
El avión ha aterrizado y se ha apagado.
El avión no puede volar porque está apagado.
```
```