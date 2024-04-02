import time
import serial
import tkinter as tk
import threading

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

def enviar_valor(valor):
    arduino.write(str(valor).encode())  
    print("Valor enviado correctamente.")
    time.sleep(0.1)

def leer_datos_desde_arduino():
    while True:
        datos = arduino.readline()
        if datos:
            procesar_datos(datos)

def procesar_datos(datos):
     print("Datos recibidos desde Arduino:", datos.decode().strip())  # De esta forma se envían mensajes que recibe el puerto serial cada cuanto apagamos/encendemos los leds/grupos

def crear_boton_circular(master, grupo):
    def on_button_click():
        enviar_valor(grupo)

    button_frame = tk.Frame(master)
    button_frame.pack(side=tk.LEFT, padx=10) 

    button = tk.Canvas(button_frame, width=80, height=80, bd=0)
    button.pack()


    button.create_oval(10, 10, 70, 70, fill="blue", outline="black")
    button.create_text(40, 40, text="Grupo {}".format(grupo), fill="white", font=("Arial", 12))

    button.bind("<Button-1>", lambda event: on_button_click())

thread_arduino = threading.Thread(target=leer_datos_desde_arduino)
thread_arduino.start()
    
def main():
    root = tk.Tk()
    root.title("Control de Grupos")

    for i in range(1, 6):
        crear_boton_circular(root, i)

    root.mainloop()

    arduino.close()

if __name__ == "__main__":
    main()
