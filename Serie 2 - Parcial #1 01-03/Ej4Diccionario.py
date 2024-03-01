# Alvaro Jesús Flores Pérez - 0901-22-1359
# Parcial #1 - Programación #3
# Cuarto ejercicio Serie 2


#Declaramos un diccionario que se llamara libro con atributos
libro = {
    'titulo': 'De la tierra a la luna',
    'autor': "Juan",
    "anio": "1890",
}

#Para agregar un atributo extra que es género tenemos la propiedad update para agregar el atributo de género
libro.update({"genero": "ficción"})


#Imprimios el libro y veremos el campo nuevo agregado
print(libro)