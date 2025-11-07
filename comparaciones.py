import time
import random

# --- 1. Implementación de Bubble Sort ---
def bubble_sort(arr):
    """Implementación del algoritmo Bubble Sort."""
    n = len(arr)
    # Recorrer todos los elementos del array
    for i in range(n):
        # El último i-ésimo elemento ya está en su lugar
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# --- 2. Función para medir el tiempo de ejecución ---
def medir_tiempo(func, lista):
    """Mide el tiempo de ejecución de una función."""
    # Crear una copia de la lista para no modificar el original
    lista_copia = list(lista)
    
    inicio = time.perf_counter()
    func(lista_copia)
    fin = time.perf_counter()
    
    # Devolver el tiempo en segundos
    return fin - inicio

# --- 3. Tamaños de las listas a probar ---
TAMAÑOS = [100, 500, 1000, 5000]

# --- 4. Ejecución de las comparaciones ---
print("Comparación de Tiempos de Ejecución: Bubble Sort vs sorted\n")

for n in TAMAÑOS:
    # Generar una lista aleatoria de tamaño 'n'
    lista_aleatoria = [random.randint(1, 10000) for _ in range(n)]
    
    # Medir Bubble Sort
    # Se le pasa la función bubble_sort como argumento
    tiempo_bubble = medir_tiempo(bubble_sort, lista_aleatoria)
    
    # Medir sorted() (usando una función lambda para que tenga la misma firma)
    # La función lambda llama a sorted() sobre una copia de la lista y la devuelve
    tiempo_sorted = medir_tiempo(lambda l: sorted(l), lista_aleatoria)
    
    # Imprimir el resultado con el formato deseado
    print(f"n = {n} → BubbleSort = {tiempo_bubble:.4f}s | sorted = {tiempo_sorted:.4f}s")