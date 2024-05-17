import tkinter as tk
import serial

# Configurar la comunicación serial
ser = serial.Serial('COM3', 9600)

def send_command(command):
    ser.write(command.encode())
    print(f"Comando enviado: {command}")

# Crear la ventana principal
root = tk.Tk()
root.title("Control del Servomotor")

# Configurar el grid para expandirse
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)

# Crear tres marcos (frames) para dividir la ventana
frame_left = tk.Frame(root, bg="lightblue", bd=2, relief=tk.SOLID)
frame_center = tk.Frame(root, bg="lightgreen", bd=2, relief=tk.SOLID)
frame_right = tk.Frame(root, bg="lightcoral", bd=2, relief=tk.SOLID)

frame_left.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
frame_center.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
frame_right.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

# Crear etiquetas (labels) que actúan como botones
label_left = tk.Label(frame_left, text="Izquierda", bg="blue", fg="white", font=("Arial", 16), width=10, height=5)
label_center = tk.Label(frame_center, text="Centro", bg="green", fg="white", font=("Arial", 16), width=10, height=5)
label_right = tk.Label(frame_right, text="Derecha", bg="red", fg="white", font=("Arial", 16), width=10, height=5)

label_left.pack(expand=True, fill=tk.BOTH)
label_center.pack(expand=True, fill=tk.BOTH)
label_right.pack(expand=True, fill=tk.BOTH)

# Asignar comandos a las etiquetas
label_left.bind("<Button-1>", lambda e: send_command('I'))
label_center.bind("<Button-1>", lambda e: send_command('C'))
label_right.bind("<Button-1>", lambda e: send_command('D'))

# Iniciar el bucle principal de Tkinter
root.mainloop()
