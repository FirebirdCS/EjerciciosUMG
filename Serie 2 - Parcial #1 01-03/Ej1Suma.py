# Alvaro Jesús Flores Pérez - 0901-22-1359
# Parcial #1 - Programación #3
# Primer ejercicio - Serie 2


#Definimos una función
def sumaParametros(lista):
    tamanio = len(lista) # Tomamos el tamaño de la lista
    suma = 0 # Declaramos una variable que sea igual a 0 para almacenar la suma de los elementos de la lista
    for i in range(0, tamanio):     # Ciclo for para recorrer cada elemento de la lista   
        suma += int(lista[i]) # Vamos sumando cada uno de estos elementos
    total = suma # Asignamos la suma a una variable total
    print(total) 
            
# Creamos un arreglo de números
arreglo = [1,2,3]
#Llamamos la función y nos mostrará el resultado de la suma
sumaParametros(arreglo)