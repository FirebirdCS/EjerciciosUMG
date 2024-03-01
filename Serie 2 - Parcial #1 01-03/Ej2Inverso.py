# Alvaro Jesús Flores Pérez - 0901-22-1359
# Parcial #1 - Programación #3
# Segundo ejercicio Serie 2

# definimos función
def invertirPalabra(palabra):
    invertido = palabra[::-1] #invertimos la palabra ingresada en el cuál hacemos slicing 
    #para recorrer cada caracter de la palabra e invertirlo de derecha a izquierda           
    print(invertido)


# Llamamos la función
invertirPalabra("python")