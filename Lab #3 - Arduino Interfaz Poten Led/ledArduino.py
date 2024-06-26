import serial
import tkinter as tk
import threading

# Configuración del puerto serial, cambia el puerto y la velocidad según tu configuración de Arduino
ser = serial.Serial('COM3', 9600)

# Función para leer datos del puerto serie
def serial_reader():
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            if data:
                handle_code(data)

# Función para encender un círculo
def turn_on_circle(circle, color):
    canvas.itemconfig(circle, fill=color)

# Función para apagar un círculo
def turn_off_circle(circle):
    canvas.itemconfig(circle, fill="white")

# Función para manejar los datos recibidos del puerto serie
def handle_code(code):
    try:
        digit = int(code)
        print("Código recibido:", digit)
        # Apagar todos los círculos y rectángulos primero
        for circle in circles:
            turn_off_circle(circle)

        # Encender el círculo correspondiente al código recibido
        if digit == 1:
            turn_on_circle(circles[0], "green")
        elif digit == 2:
            turn_on_circle(circles[1], "blue")
        elif digit == 3:
            turn_on_circle(circles[2], "yellow")
        # Encender el cuadrado correspondiente al código recibido y su modo
        if digit == 5:
            canvas.create_rectangle(301, 150, 350, 200, outline="black", width=2, fill="red")
        elif digit == 6:
            canvas.create_rectangle(371, 150, 420, 200, outline="black", width=2, fill="red")
        elif digit == 7:
            canvas.create_rectangle(441, 150, 490, 200, outline="black", width=2, fill="red")
        elif digit == 8:
            canvas.create_rectangle(301, 150, 350, 200, outline="black", width=2, fill="white")
            canvas.create_rectangle(371, 150, 420, 200, outline="black", width=2, fill="white")
            canvas.create_rectangle(441, 150, 490, 200, outline="black", width=2, fill="white")
        # Actualizar el valor de la barra de potenciómetro
        update_bar_graph(digit)
    except ValueError:
        print("Mensaje desde Arduino:", code.strip())




# Función para actualizar la barra de potenciómetro
def update_bar_graph(value):
    # Normalizar el valor para que esté en el rango de 0 a 1
    normalized_value = value / 1023
    # Calcular las coordenadas de la barra
    x0 = 50
    y0 = 275
    x1 = 50 + normalized_value * 500 
    y1 = 325
    # Calcular el color en función del valor del potenciómetro
    color = '#%02x%02x%02x' % (int(255 - (normalized_value * 255)), int(normalized_value * 255), 0)

    # Actualizar las coordenadas y el color de la barra
    canvas.coords(bar, x0, y0, x1, y1)
    canvas.itemconfig(bar, fill=color)


# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("Botón Controlador")
root.geometry("600x400")

# Configuración de la gráfica de barras
canvas = tk.Canvas(root, width=600, height=500)
canvas.pack()
bar = canvas.create_rectangle(50, 400, 50, 450, fill='green')

# Configuración de los circulos
circles = []
for i in range(3):
    circle = canvas.create_oval(50 + i * 70, 150, 100 + i * 70, 200, outline="black", width=2, fill="white")
    canvas.create_text(75 + i * 70, 175, text=str(i+1), font=("Arial", 12))
    circles.append(circle)

# Rectángulos
rectangle1 = canvas.create_rectangle(301, 150, 350, 200, outline="black", width=2, fill="white")
rectangle2 = canvas.create_rectangle(371, 150, 420, 200, outline="black", width=2, fill="white")
rectangle3 = canvas.create_rectangle(441, 150, 490, 200, outline="black", width=2, fill="white")


# Labels

title_text = tk.Label(root, text="Laboratorio #3")
title_text.place(x=250, y=25)


button_text = tk.Label(root, text="LEDs")
button_text.place(x=50, y=100)

button_text = tk.Label(root, text="Modo")
button_text.place(x=300, y=100)

pot_text = tk.Label(root, text="Potenciómetro")
pot_text.place(x=50, y=250)


canvas.create_text(325, 210, text="Inorden", font=("Arial", 11))
canvas.create_text(390, 210, text="Postorden", font=("Arial", 11))
canvas.create_text(470, 210, text="Preorden", font=("Arial", 11))

# Crear y ejecutar el hilo para leer datos del puerto serie
serial_thread = threading.Thread(target=serial_reader)
serial_thread.daemon = True
serial_thread.start()

# Ejecutar la aplicación Tkinter
root.mainloop()
