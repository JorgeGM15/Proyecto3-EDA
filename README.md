# Planificador de Trabajos con Algoritmos y Combinatoria

Este proyecto es una herramienta de línea de comandos desarrollada en Python que implementa algoritmos de planificación para optimizar la programación de un conjunto de trabajos con horarios de inicio y fin definidos.

---

## 📜 Descripción

El programa analiza una lista de trabajos y ofrece dos tipos de soluciones óptimas:

1.  **Maximizar la Cantidad de Trabajos**: Encuentra el mayor número de trabajos que se pueden realizar sin que sus horarios se superpongan.
2.  **Maximizar el Tiempo Ocupado**: Identifica los trabajos de mayor duración y encuentra todas las combinaciones posibles de estos que se pueden programar sin conflictos.

---

## 🧠 Algoritmos Utilizados

* **Merge Sort**: Un algoritmo eficiente de ordenamiento (divide y vencerás) para organizar los trabajos por su hora de inicio, un paso fundamental para el algoritmo voraz.
* **Algoritmo Voraz (Greedy)**: Implementa la solución clásica al "problema de selección de actividades" para determinar el conjunto de trabajos compatibles que maximiza la cantidad de tareas realizadas.
* **Análisis Combinatorio**: Utiliza la generación de conjuntos potencia para explorar todas las posibles agendas formadas exclusivamente por los trabajos de mayor duración y filtra aquellas que son válidas (sin solapamientos).

---

## ✨ Características

* **Entrada de Datos Interactiva**: Permite al usuario ingresar el número de trabajos y los detalles de cada uno.
* **Validación de Entradas**: Asegura que los horarios ingresados sean lógicos (inicio < fin) y estén dentro de un rango de 24 horas.
* **Doble Análisis**: Proporciona dos perspectivas diferentes para la optimización del horario.
* **Reporte de Conflictos**: Alerta al usuario si algunos de los trabajos ingresados se superponen entre sí.

---

## 🚀 Cómo Ejecutar el Programa

1.  Asegúrate de tener **Python 3** instalado en tu sistema.
2.  Guarda el código en un archivo, por ejemplo `planificador.py`.
3.  Abre una terminal o consola de comandos en el directorio donde guardaste el archivo.
4.  Ejecuta el script con el siguiente comando:
    ```bash
    python planificador.py
    ```
5.  Sigue las instrucciones en pantalla para ingresar los datos de los trabajos. El programa mostrará los resultados del análisis al final.
