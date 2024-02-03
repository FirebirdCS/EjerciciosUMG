class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def ha_aprobado(self):
        if self.nota >= 60:
           return "Aprobado"
        else:
           return "No aprobado"

estudiante1 = Estudiante("Juan", 20, 75)
estudiante2 = Estudiante("Ana", 22, 45)

print(f"{estudiante1.nombre} ha aprobado?: {estudiante1.ha_aprobado()}")
print(f"{estudiante2.nombre} ha aprobado? : {estudiante2.ha_aprobado()}")
