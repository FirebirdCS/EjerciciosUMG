# Ejercicio #1

#Definimos la clase de pila
class Pila:
    def __init__(self):
        self.items = []
        # Definimos nuestra clase con un arreglo vacío llamado
    def push(self,elemento):
        self.items.append(elemento)
        # Metodo en el cual introduciremos elementos a nuestro arreglo de items con el atributo de append
    def esta_vacia(self):
        return len(self.items) == 0
        # Metodo en el cuál sabremos si nuestra pila tiene elementos o no con la función de len
    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        # Verificamos si la pila no esta vacía, si no es así, eliminaremos su ultimo elemento.
        # El atributo pop,por defecto, elimina el ultimo elemento
        else:
            print("La pila está vacía")
        # Si la pila esta vacía, nos mostrará un mensaje de que la pila esta vacía
    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]
        # Si la pila  no esta vacía entonces recorrera la pila y arrojará el ultimo elemento de la pila
        else:
            print("La pila está vacía")
        # Si la pila esta vacía, nos mostrará un mensaje de que la pila esta vacía
    def revertir_lista(self, lista):
        for elemento in lista:
            self.push(elemento)
            # Agregamos cada elemento de la pila
        # Inicializamos una lista para almacenar los elementos que vamos a revertir
        lista_revertida = []
        while not self.esta_vacia():
            lista_revertida.append(self.pop())
            # Sacamos los elementos de la pila y los agregamos a la lista revertida con el atributo pop
        return lista_revertida
        # Devolvemos la lista con los elementos revertidos
    
# Casos de ejemplo

miPila = Pila()

# Pila revertida

lista_original = [1, 2, 3, 4, 5]
lista_invertida = miPila.revertir_lista(lista_original)
print(lista_original)
print(lista_invertida)

# Ver ultimo elemento de la pila

miPila.push(1)
miPila.push(2)
miPila.push(3)

ultimoEl = miPila.peek()

print("El ultimo elemento es: ", ultimoEl)

