import random

n = random.randint(0, 10)
num = int(input("Ingrese un número: "))

while n != num:
    print("No adivinaste el número!")
    num = int(input("Ingrese un número: "))

print(f"Número acertado!  {num} == {n}")