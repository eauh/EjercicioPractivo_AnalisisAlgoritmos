class Burbuja:
    def ordenar(self, lista):
        cantidad = len(lista)
        print("Lista inicial:", lista)
        for x in range(cantidad):
            for y in range((cantidad-1)-x):
                if lista[y] > lista[y + 1]:
                    lista[y], lista[y + 1] = lista[y + 1], lista[y]
        print("Lista ordenada:", lista)


