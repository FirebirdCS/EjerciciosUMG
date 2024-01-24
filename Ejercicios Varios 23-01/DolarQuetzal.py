dolar = float(input("Ingresa el monto en dólares: "))

if dolar < 0:
    print("Ingresa un monto positivo")
else: 
    quetzal = float(dolar * 7.82) 
    print("La conversión de divisas de dólar a quetzal es de: " +  "Q" +str(quetzal) )
