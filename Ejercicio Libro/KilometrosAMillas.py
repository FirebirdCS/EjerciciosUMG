def conv(km):
    millas = float(km * 0.6214) 
    return millas

km = int(input("Ingresa la distancia recorrida en kilómetros: "))
millas = conv(km)
print("La distancia recorrida en millas es de: " + str(millas))