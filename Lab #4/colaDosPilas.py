# Ejercicio #4

# Declaramos nuestra clase
class ColaConPilas:
    def __init__(self):
        # Definimos dos arreglos en los cuales por uno entraran los elementos y por el otro saldran los elementos
        self.pila_entrada = []
        self.pila_salida = []

    def esta_vacia(self):
        # Declaramos un método para verificar si ambas pilas no estan vacías
        return len(self.pila_entrada) == 0 and len(self.pila_salida) == 0

    def enqueue(self, elemento):
        # Declaramos un método para meter elementos a nuestra pila con el atributo append
        self.pila_entrada.append(elemento)

    def dequeue(self):
         # Verificamos si la pila de salida está vacía
        if not self.pila_salida:
             # Si la pila de salida está vacía verificamos si la pila de entrada también está vacía
            if not self.pila_entrada:
                print("Ambas colas están vacías")
            # Mientras hay elementos en la pila de entrada, los movemos a la pila de salida
            while self.pila_entrada:
                # Utilizamos el atributo append para añadir el ultimo elemento que quitamos de la pila de entrada, utilizando el atributo pop.
                self.pila_salida.append(self.pila_entrada.pop())
             # Devolvemos el elemento desencolado de la pila de salida
        return self.pila_salida.pop()

# Caso de ejemplo
cola = ColaConPilas()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)

print("Cola después de enqueue:" , "Entrada: " , cola.pila_entrada , "Salida: " , cola.pila_salida)

elemento_atendido = cola.dequeue()
print("Elemento atendido:", elemento_atendido)
print("Cola después de dequeue:" , "Entrada: " , cola.pila_entrada , "Salida: " , cola.pila_salida)

# Podemos volver a descolar otro elemento haciendo uso del metodo de cola.dequeue() 
# Al imprimir en pantalla la pila de salida vemos que el 3 esta delante del 2, esto sucede al momentor de meter a la pila de salida el primer elemento de la pila de entrada
# Aunque siempre terminará escogiendo el primer elemento que haya entrado a la cola de salida