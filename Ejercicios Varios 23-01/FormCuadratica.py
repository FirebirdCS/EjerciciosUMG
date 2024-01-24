from math import sqrt

a = float(input("Ingresa la variable a  (x^2): "))
b = float(input("Ingresa la variable b (x): "))
c = float(input("Ingresa la variable c : "))


opPos = (b**2)-(4*a*c)
if opPos < 0:
    print("La raíz es un número imaginario (negativo), no se puede seguir operando")
else: 
    raiz = float(sqrt(opPos))
    x1 = (-b + raiz) / (2*a)
    x2 = (-b - raiz) / (2*a)

    print("La primera incógnita es: " +str(x1))
    print("La segunda incógnita es: "+str(x2))

