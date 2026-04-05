# Laboratorio 1: Arquitectura y Organización de Computadores

## 1. Integrantes
* **Nombre:** Isidora Villegas | **Rol:** 202203026-7
* **Nombre:** Héctor Chanampe | **Rol:** 202304613-2
* **Paralelo:** 201
## 2. Especificación de los Algoritmos y Desarrollo Realizado
Para este laboratorio, se implementó un decodificador respetando estrictamente la prohibición de utilizar bases puente o funciones nativas de conversión de Python (como `bin()`, `hex()`, etc.). El desarrollo se estructuró de la siguiente manera:

* **Lectura y Sanitización:** El programa lee el flujo de texto continuo y extrae los valores numéricos mediante sus prefijos (`*`, `&`, `#`, `!`). Durante esta fase de extracción, se aplicó una normalización inmediata (usando `.upper()`) para garantizar que todas las letras hexadecimales ingresen al sistema en mayúsculas.s.
* **Conversiones Directas (Bases 2, 8 y 16):** Para las transformaciones entre sistemas cuyas bases son potencias de 2, se implementó el algoritmo nativo de **agrupación y expansión de bits**. Se utilizaron mapas de diccionarios (ej. `bin_hex` y `oct_bin`) para traducir instantáneamente los bloques de bits. 
    * *Octal a Hexadecimal (y viceversa):* Se realiza expandiendo cada dígito a su representación binaria pura y reagrupando la cadena resultante en bloques de 4 (o 3) bits de derecha a izquierda, rellenando con ceros a la izquierda cuando es necesario mediante la operación de módulo (`len % 4` o `len % 3`).
* **Conversiones Matemáticas (Base 10):** Para interactuar con el sistema decimal, se utilizó el método algorítmico clásico:
    * *Hacia Base 10:* Suma de productos utilizando las potencias de la base de origen correspondientes a la posición de cada dígito.
    * *Desde Base 10:* Algoritmo de divisiones sucesivas por la base de destino (2, 8 o 16), capturando los residuos.
* **Filtrado (ASCII):** Se procesaron todos los valores extraídos para la visualización en tabla, pero para el mensaje final se evaluó su equivalente decimal en el rango de caracteres requerido ($32 \le x \le 126$).

## 3. Supuestos Utilizados
* Se asume que el archivo de entrada se llama exactamente `notas_dm.txt` y se encuentra ubicado en el mismo directorio (carpeta) desde el cual se está ejecutando el script `LAB1_202304613-2_202203026-7.py`.
* Se asume que el usuario ingresará un valor numérico válido (2, 8, 10 o 16) cuando el programa solicite la "Base de Visualización" por consola.
* Se asume que, en caso de encontrar un prefijo válido seguido inmediatamente por caracteres que no corresponden a su base (ruido absoluto, ej. `*A8`), el programa simplemente ignorará ese segmento sin generar un número vacío en la tabla de salida.
