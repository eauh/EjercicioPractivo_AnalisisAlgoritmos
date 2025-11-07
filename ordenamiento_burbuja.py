# Ordenamiento Burbuja en Python

datos = [45, 12, 78, 23, 56, 89, 34, 67, 90, 11,
32, 76, 54, 21, 65, 87, 43, 98, 29, 71,
38, 15, 82, 49, 97, 26, 63, 19, 85, 52]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("Lista original:", datos)
ordenada = bubble_sort(datos[:])  # usamos copia
print("Lista ordenada (burbuja):", ordenada)

