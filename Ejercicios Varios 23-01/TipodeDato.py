dato = input("Ingresa un valor: ")


if dato.isdigit():
    print("Debes ingresar un número entero.")
elif dato.replace(".", "").isdigit():
    print("Debes ingresar un número decimal.")
elif dato == "true" or dato == "false":
    print("Debes ingresar un valor booleano.")
else:
    print("Debes ingresar una cadena de texto.")
