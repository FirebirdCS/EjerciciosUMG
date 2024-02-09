# Ejercicio #3

# Definimos el metodo para comprobar los parentésis
def parentesis_Valido(lista):
    pila = [] # Creamos un arreglo vacío donde entraran las listas que pasemos
    parentesis = {'{' : '}', '[' : ']' , '(' : ')'} # Definimos un diccionario en el cual comprobará cada llave de apertura con su llave de cierre
    for elemento in lista: #Iteramos cada elemento dentro de nuestra lista
        if elemento in parentesis: # Verificamos si el elemento esta dentro de nuestro diccionario
            pila.append(elemento) # Si es un si, entonces agregamos a nuestra pila el elemento
        elif len(pila) == 0 or elemento != parentesis[pila.pop()]: 
        # Verificamos si no hay elementos en nuestra pila o si el elemento no es igual a la llave de cierre del diccionario con el atributo pop()
            return False # Retornamos falso si no se cumple las condiciones
    return len(pila) == 0 # No retornamos nada si en esta caso la pila esta vacía

# Casos de ejemplo en los cuales pasamos una lista de parentesis

print(parentesis_Valido("()[]{}"))
print(parentesis_Valido("()[]{}["))
print(parentesis_Valido("([])"))
print(parentesis_Valido("([{}])"))
print(parentesis_Valido("([{])}"))
print(parentesis_Valido("){}"))