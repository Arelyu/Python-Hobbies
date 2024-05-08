# Este script descarga un video de youtube
# Extrae el audio en formato mp3 y elimina el video despues de la conversion

import tkinter as tk # tkinter para la interfaz grafica
from tkinter import filedialog # filedialog para los dialogos de abrir y guardar archivo
from pytube import YouTube # pytube para descargar video y audio de youtube
from moviepy.editor import * # moviepy para extraer el audio de los videos
import os # os para interactuar con el sistema, crear, borrar los archivos temporales

def descargar_audio():
    url = url_entry.get()
    output_path = output_path_entry.get()
    
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_path = audio_stream.download(output_path=output_path, filename="temp_audio")
        
        # Convertir el archivo de audio descargado a formato MP3
        clip = AudioFileClip(audio_path)
        mp3_path = output_path + "/audio.mp3"
        clip.write_audiofile(mp3_path)
        
        status_label.config(text="¡Descarga y conversión de audio completadas!")
    except Exception as e:
        status_label.config(text=f"Ocurrió un error al descargar y convertir el audio: {str(e)}")
    
    # Eliminar el archivo temporal después de la conversión
    os.remove(audio_path)

def seleccionar_directorio():
    output_path = filedialog.askdirectory()
    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, output_path)

# Crear la ventana principal
root = tk.Tk()
root.title("Descargar Audio de YouTube")

# Crear y posicionar los widgets
url_label = tk.Label(root, text="URL del video de YouTube:")
url_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

output_path_label = tk.Label(root, text="Directorio de salida:")
output_path_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

output_path_entry = tk.Entry(root, width=50)
output_path_entry.grid(row=1, column=1, padx=5, pady=5)

output_path_button = tk.Button(root, text="Seleccionar", command=seleccionar_directorio)
output_path_button.grid(row=1, column=2, padx=5, pady=5)

descargar_button = tk.Button(root, text="Descargar Audio", command=descargar_audio)
descargar_button.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
