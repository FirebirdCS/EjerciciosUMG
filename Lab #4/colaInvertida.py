# Ejercicio #5

from collections import deque

#Definimos nuestro método
def revertir_mitad_cola(cola):
    # Verificamos si la cola está vacía o tiene un solo elemento, si es así imprimiremos un mensaje
    if len(cola) <= 1:
        print("La cola ya está invertida o tiene menos de dos elementos.")
        return

    # Calculamos la mitad de la longitud de la cola
    mitad = len(cola) // 2

    # Utilizamos una pila para almacenar la segunda mitad de los elementos
    pila_auxiliar = deque()

    # Encolamos la segunda mitad de los elementos dentro de la pila auxiliar
    # Uso un un guión bajo dentro del for esto es para que decir que no tenemos una variable en el cual el valor va a ser ignorado, necesario para este ejercicio
    for _ in range(mitad):
        # Vamos a meter dentro de la pila auxiliar los elementos que esten en la mitad del arreglo comenzando de derecha a izquierda con el atributo pop
        pila_auxiliar.append(cola.pop())

    # Mientras haya elementos en la pila auxiliar vamos a encolar de nuevo los elementos que esten en pila_auxiliar a la cola, comenzando de izquierda a derecha para evitar que se repita la cola original.
    while pila_auxiliar:
        cola.append(pila_auxiliar.popleft()) # Utilizamos el atributo append y popleft para meter los elementos de izquierda a derecha.

# Caso de ejemplo
cola_ejemplo = deque([1, 2, 3, 4, 5, 6])
print("Cola original:", list(cola_ejemplo))
revertir_mitad_cola(cola_ejemplo)
print("Cola después de revertir la mitad:", list(cola_ejemplo))
