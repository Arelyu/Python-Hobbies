# Este script ejecuta "n" cantidad de veces un click derecho por segundo
# Asigna una tecla para activar y desactivar la ejecucion automatica del script

import tkinter as tk # tkinter para la interfaz grafica
import threading # threading para usar hilos
import time # time para manjear los tiempos de ejecucion de la funcion
from pynput import keyboard, mouse # pynput para usar los eventos del teclado y mouse

autoclick = False # Estado inicial
speed = 10  # Clicks por segundo
key = keyboard.KeyCode.from_char('z')  # Tecla para activar/desactivar

# Controlador de teclado y mouse
keyboard_listener = None

# Función para ejecutar los clicks
def autoclicker():
    m = mouse.Controller()  # Controlador del mouse
    while True:
        if autoclick:
            m.click(mouse.Button.right)  # Hacer clic derecho
            time.sleep(1 / speed)  # Ritmo según la velocidad
        else:
            time.sleep(0.1)  # Pequeña espera para reducir el uso de recursos

# Activar/desactivar los clicks con la tecla asignada
def toggle_autoclick(key):
    if key == key:
        global autoclick
        autoclick = not autoclick
        update_status()  # Actualizar el mensaje si esta activado o desactivado

# Actualizar el estado en la interfaz gráfica
def update_status():
    if autoclick:
        status_label.config(text="Activado", fg="#a5dc86")
    else:
        status_label.config(text="Desactivado", fg="#f27474")

# Iniciar el listener del teclado
def start_keyboard_listener():
    global keyboard_listener
    if keyboard_listener:
        keyboard_listener.stop()  # Detener el listener existente
    keyboard_listener = keyboard.Listener(on_press=toggle_autoclick)
    keyboard_listener.start()

# Aplicar la velocidad de clics
def apply_speed():
    global speed
    try:
        speed = int(speed_entry.get())
        error_label.config(text="", fg="white")
    except ValueError:
        speed = 10
        error_label.config(text="Valor inválido para la velocidad, usando 10", fg="orange")

# Aplicar la tecla de activación
def apply_activation_key():
    global key
    key_char = activation_key_entry.get().lower()  # Obtener la tecla preferida del usuario
    if len(key_char) == 1 and key_char.isalpha():
        key = keyboard.KeyCode.from_char(key_char)
        start_keyboard_listener()  # Reiniciar el listener del teclado para aplicar la nueva tecla
        error_label.config(text="", fg="white")
    else:
        error_label.config(text="Tecla no válida. Debe ser una letra.", fg="orange")

# Cerrar el programa y detener el listener
def close_app():
    global keyboard_listener
    if keyboard_listener:
        keyboard_listener.stop()
    root.destroy()  # Cierra la ventana y termina la aplicación

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Fastpy")

# Color de fondo
root.configure(bg="#4b4d53")

# Indicador de estado
status_label = tk.Label(root, text="Desactivado", font=("Helvetica", 12, "bold"), fg="#f27474", bg="#4b4d53")
status_label.pack(pady=10)

# Entrada para ajustar la velocidad de clics por segundo
speed_label = tk.Label(root, text="Clics por segundo:", fg="white", bg="#4b4d53")
speed_label.pack(pady=5)
speed_entry = tk.Entry(root)
speed_entry.insert(0, "10")
speed_entry.pack(pady=5)

# Botón para aplicar la velocidad de clics
apply_speed_button = tk.Button(root, text="Aplicar Velocidad", command=apply_speed, bg="#3a3c3f", fg="white")
apply_speed_button.pack(pady=5)

# Entrada para establecer la tecla de activación
activation_key_label = tk.Label(root, text="Tecla para activar/desactivar:", fg="white", bg="#4b4d53")
activation_key_label.pack(pady=5)

activation_key_entry = tk.Entry(root)
activation_key_entry.insert(0, "z")  # Tecla por defecto
activation_key_entry.pack(pady=5)

# Botón para aplicar la tecla de activación
apply_activation_button = tk.Button(root, text="Aplicar Tecla", command=apply_activation_key, bg="#3a3c3f", fg="white")
apply_activation_button.pack(pady=5)

# Etiqueta para mostrar errores o advertencias
error_label = tk.Label(root, text="", fg="orange", bg="#4b4d53", font=("Helvetica", 10, "italic"))

# Botón para cerrar el programa
close_button = tk.Button(root, text="Cerrar", command=close_app, bg="#3a3c3f", fg="white")
close_button.pack(pady=5)

# Iniciar el hilo del programa y el listener del teclado
autoclicker_thread = threading.Thread(target=autoclicker, daemon=True)
autoclicker_thread.start()

start_keyboard_listener()  # Iniciar el listener del teclado

# Ejecución de la interfaz gráfica
root.mainloop()
