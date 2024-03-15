import time
import serial


arduino = serial.Serial('COM3', 9600)
time.sleep(2)


while True:
    valor = input("Ingrese el valor que desea enviar al Arduino (ingrese 'q' para salir): ")
    

    if valor.lower() == 'q':
        print("Saliendo del programa...")
        break
    

    arduino.write(str.encode(valor))
    print("Valor enviado correctamente.")

arduino.close()