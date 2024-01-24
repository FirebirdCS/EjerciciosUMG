hora = float(input("Ingresa la hora actual: "))

minutos = float(input("Ingresa los minutos actuales: "))

if hora < 0 or minutos < 0:
    print("No puedes ingresar horas negativas")
else:
    segHora = hora * 3600
    segMin = minutos * 60

    seg = segHora + segMin

    print("Los segundos transcurridos durante el día son: " + str(seg) + " segundos")