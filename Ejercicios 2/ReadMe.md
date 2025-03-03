¡Claro! Aquí tienes un enunciado claro y detallado para pedir la implementación de este código:

---

### **Enunciado del Ejercicio**:

#### **Objetivo**:
Implementar un sistema de generación y validación de contraseñas aplicando el **Principio de Inversión de Dependencias (DIP)**. El sistema debe permitir generar contraseñas aleatorias de una longitud específica y verificar si son fuertes según ciertos criterios.

---

#### **Requisitos**:

1. **Clase `Password`**:
   - Atributos:
     - `longitud`: Longitud de la contraseña (por defecto 8).
     - `contraseña`: La contraseña generada.
   - Constructores:
     - Un constructor por defecto que genera una contraseña de longitud 8.
     - Un constructor que recibe la longitud y genera una contraseña aleatoria con esa longitud.
   - Métodos:
     - `es_fuerte()`: Devuelve `True` si la contraseña es fuerte y `False` en caso contrario. Para que una contraseña sea fuerte, debe cumplir:
       - Más de 2 letras mayúsculas.
       - Más de 1 letra minúscula.
       - Más de 5 números.
     - `generar_password()`: Genera una contraseña aleatoria con la longitud actual.
     - Métodos `get` para `contraseña` y `longitud`.
     - Método `set` para `longitud` (al cambiar la longitud, se debe regenerar la contraseña).

2. **Interfaz `PasswordGenerator`**:
   - Define los métodos abstractos:
     - `generar_password(longitud)`: Genera una contraseña aleatoria.
     - `es_fuerte(contraseña)`: Verifica si la contraseña es fuerte.

3. **Clase `GeneradorPasswordSimple`**:
   - Implementa la interfaz `PasswordGenerator`.
   - Usa letras (mayúsculas y minúsculas) y números para generar contraseñas aleatorias.
   - Implementa la lógica para verificar si una contraseña es fuerte.

4. **Clase Ejecutable**:
   - Crea un array de objetos `Password` con un tamaño definido por el usuario.
   - Pide al usuario la longitud de las contraseñas antes de generarlas.
   - Crea un array de booleanos que indique si cada contraseña es fuerte.
   - Muestra cada contraseña y si es fuerte, usando el formato:
     ```
     contraseña1 valor_booleano1
     contraseña2 valor_booleano2
     ...
     ```

---

#### **Ejemplo de Entrada/Salida**:

**Entrada**:
```
Introduce el tamaño del array de contraseñas: 3
Introduce la longitud de las contraseñas: 10
```

**Salida**:
```
aB3dE7fG9h True
XyZ1aB2cD3 False
QwEr5Ty7Ui False
```

---

#### **Recomendaciones**:
- Aplica el **Principio de Inversión de Dependencias (DIP)**: La clase `Password` debe depender de la abstracción `PasswordGenerator`, no de una implementación concreta.
- Usa la biblioteca `random` y `string` de Python para generar contraseñas aleatorias.
- Asegúrate de que el código sea modular, fácil de leer y seguir las buenas prácticas de programación.

---

#### **Notas Adicionales**:
- El sistema debe ser flexible para permitir futuras implementaciones de generadores de contraseñas (por ejemplo, usando símbolos especiales).
- El código debe estar bien documentado y seguir un estilo limpio (PEP 8).

---

Este enunciado proporciona una guía clara y estructurada para implementar el código solicitado. ¡Espero que te sea útil! 😊