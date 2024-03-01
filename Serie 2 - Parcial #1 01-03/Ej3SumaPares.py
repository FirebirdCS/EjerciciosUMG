# Alvaro Jesús Flores Pérez - 0901-22-1359
# Parcial #1 - Programación #3
# Tercer ejercicio Serie 2

# Definimos función el cual entrara una lista de numeros
def sumaParametrosPares(lista):
    tamanio = len(lista) # Declaramos variable la cual tomara el tamaño del arreglo
    suma = 0  # Declaramos una variable que sea igual a 0 para almacenar la suma de los elementos de la lista
    for i in range(0, tamanio): # Ciclo for para recorrer cada elemento de la lista   
        if(i % 2 != 0): # Verificamos por cada elemento, si este elemento es par o no si su division es igual a cero como residuo
            suma += lista[i] # Vamos sumando cada uno de los números pares
    total = suma # Asignamos la suma a una variable total
    print(total)

        
# Creamos un arreglo 
arreglo = [1,2,3,4,5,6,7,8,9,10,11]
# Llamamos la función y metemos como parametro nuestro arreglo
sumaParametrosPares(arreglo) # El total de la suma debe ser 30