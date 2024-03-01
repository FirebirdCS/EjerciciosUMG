arreglo = [9,5,1]

tamanio = len(arreglo)
swapped = True

while swapped:
    swapped = False
    for i in range(1, tamanio):
        if(arreglo[i - 1] > arreglo[i]):
            temp = arreglo[i - 1]
            arreglo[i - 1] = arreglo[i]
            arreglo[i] = temp
            swapped = True
        

print(arreglo)


