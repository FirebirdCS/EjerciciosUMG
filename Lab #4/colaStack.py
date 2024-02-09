# Ejercicio #2

import time
from collections import deque

# Declaramos nuestra clase de cola
class Cola:
    def __init__(self):
        self.items = deque()
        # Inicializamos nuestra cola
    def esta_vacia(self):
        return len(self.items) == 0
        # Metodo en el cuál sabremos si nuestra cola tiene elementos o no con la función de len
    def enqueue(self, elemento):
        self.items.append(elemento)
        # Metodo con el cual añadimos elementos a nuestra cola
    def dequeue(self):
         # Metodo con el cual eliminamos los primeros elementos de nuestra cola
        if not self.esta_vacia():
            # Entramos en un bucle mientras que la cola no este vacía
            return self.items.popleft()  # Eliminamos el primer elemento de la cola
        else:
            print("La cola está vacía")
            # Si la cola esta vacía, nos mostrará un mensaje de que la cola esta vacía
    def front(self):
        if not self.esta_vacia():
             # Metodo con el cual vemos el primer elemento de nuestra cola
            return self.items[0]
        else:
            print("La cola está vacía")
             # Si la cola esta vacía, nos mostrará un mensaje de que la cola esta vacía
            
    def simular_proceso(self):
         # Metodo con el cual simulamos una  cola y vamos eliminando uno por uno cada elemento de la cola.
        while not self.esta_vacia():
            # Entramos en un bucle mientras que la cola no este vacía
            cliente_actual = self.front() # Agarramos el primer elemento de la cola.
            print(f"Atendiendo a: {cliente_actual}")
            self.dequeue() # Descolamos el primer elemento de la cola.
            time.sleep(1) # Añadimos un segundo de espera entre cada elemento eliminado

# Caso de ejemplo 

fila_espera = Cola()
fila_espera.enqueue("Cliente 1")
fila_espera.enqueue("Cliente 2")
fila_espera.enqueue("Cliente 3")

print("Fila de espera inicial:", fila_espera.items)
fila_espera.simular_proceso()
print("Ya no hay gente en cola: ", fila_espera.items)
