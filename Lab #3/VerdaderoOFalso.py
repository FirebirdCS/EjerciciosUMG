def VerdaderoOFalso(a, b):
    suma = a + b
    if suma % 2 == 0:
        return True
    else:
        return False
    
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

res = VerdaderoOFalso(num1, num2)
print(res)