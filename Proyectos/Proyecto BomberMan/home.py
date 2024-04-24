from tkinter import *  # Tkinter
import tkinter as tk  # Tkinter
from PIL import Image, ImageTk  # Imágenes
from tkinter.font import Font  # Fuentes
import os  # Manejar rutas y archivos
import subprocess  # Abrir otros .py
##########################################################################################################
# Guardar en txt
def guardar_nombre_jugador(nombre): # Función para guardar el nombre del jugador en un archivo
    with open('nombre_jugador.txt', 'w') as file: # Escribe el nombre en el txt
        file.write(nombre)

def guardar_skin_seleccionada(skin): # Función para seleccionar la skin y guardarla en un archivo
    with open("skin_seleccionada.txt", "w") as file: # Escribe la skin seleccionada en el txt
        file.write(skin)
##########################################################################################################
#Iniciar Juego
def iniciar_juego(): # Función para iniciar el juego
    if skin_var.get() == '':
        skin_seleccionada = "Dutch"  # Skin predeterminada si no se selecciona ninguna
    else:
        skin_seleccionada = skin_var.get()  # Obtener la skin seleccionada
    guardar_skin_seleccionada(skin_seleccionada)  # Guardar la skin seleccionada en el archivo
    nombre_jugador = entry_name.get()  # Obtener el nombre del jugador
    guardar_nombre_jugador(nombre_jugador)  # Guardar el nombre del jugador en el archivo
    subprocess.Popen(["python", "bombertest.py"])  # Ejecutar el juego
    window.destroy()  # Cerrar la ventana principal al iniciar el juego
##########################################################################################################
#Vntana principal
window = tk.Tk()  # Crear la ventana principal
window.title("Selección de Nombre y Skin")  # Configurar el título de la ventana
window.config(bg="black")  # Configurar el color de fondo de la ventana
window.attributes('-fullscreen', True)  # Configurar la ventana para que sea de pantalla completa
##########################################################################################################
#Fondo
def cargarImagen(nombre, width, height): # Cargar la imagen
    ruta = os.path.join('images/wallpaper', nombre)  # Obtener la ruta completa de la imagen
    imagen = Image.open(ruta)  # Abrir la imagen
    imagen = imagen.resize((width, height), resample=Image.LANCZOS)  # Redimensionar la imagen
    return ImageTk.PhotoImage(imagen)  # Devolver la imagen como un objeto ImageTk

def actualizarImagen(event): # Función para actualizar la imagen de fondo al cambiar el tamaño de la ventana
    global imagen1  # Definir la imagen como global para poder modificarla
    width = event.width  # Obtener el ancho de la ventana al cambiar su tamaño
    height = event.height  # Obtener el alto de la ventana al cambiar su tamaño
    imagen1 = cargarImagen("fondo2.png", width, height)  # Cargar una nueva imagen redimensionada
    LabelFondo.config(image=imagen1)  # Configurar la etiqueta de imagen con la nueva imagen

imagen1 = cargarImagen("fondo2.png", window.winfo_width(), window.winfo_height())  # Cargar la imagen de fondo
LabelFondo = Label(window, image=imagen1)  # Crear una etiqueta de imagen
LabelFondo.place(x=0, y=0, relwidth=1, relheight=1)  # Colocar la etiqueta de imagen en toda la ventana
window.bind("<Configure>", actualizarImagen)  # Enlazar la función de actualización al cambio de tamaño de ventana
##########################################################################################################
#Canvas, label y entry
canvas_data = Frame(window, bg="black")  # Crear un marco con fondo negro
canvas_data.pack(side="left", padx=(200, 0), pady=(330, 0))  # Empaquetar el marco en la ventana principal

font_button = Font(family="Courier New", size=20, weight="bold")  # Configurar la fuente para los botones

label_name = tk.Label(canvas_data, text="NOMBRE:", font=font_button, bg="black", fg="white")  # Crear etiqueta para el nombre
label_name.pack()  # Empaquetar la etiqueta en el marco

entry_name = tk.Entry(canvas_data, font=font_button, justify="center")  # Crear entrada para el nombre
entry_name.pack(pady=(0, 30))  # Empaquetar la entrada en el marco con espacio en la parte inferior

label_skin = tk.Label(canvas_data, text="SELECCIONA UNA SKIN:", bg="black", font=font_button, fg="white")  # Crear etiqueta para seleccionar skin
label_skin.pack()  # Empaquetar la etiqueta en el marco
##########################################################################################################
#Botones
Font_Play = Font(family="Courier New", size=24, weight="bold")  # Configurar la fuente para el botón PLAY
skin_var = tk.StringVar()  # Variable para almacenar la skin seleccionada

button_skin1 = tk.Radiobutton(canvas_data, font=font_button, text="DUTCH", variable=skin_var, value="Dutch", padx=9)  # Botón para skin Dutch
button_skin1.pack(pady=5)  # Empaquetar el botón en el marco

button_skin2 = tk.Radiobutton(canvas_data, font=font_button, text="JULIOS", variable=skin_var, value="Julios")  # Botón para skin Julios
button_skin2.pack(pady=5)  # Empaquetar el botón en el marco

button_skin3 = tk.Radiobutton(canvas_data, font=font_button, text="NEKROS", variable=skin_var, value="Nekros")  # Botón para skin Nekros
button_skin3.pack(pady=5)  # Empaquetar el botón en el marco

button_play = tk.Button(canvas_data, font=Font_Play, text="PLAY", command=iniciar_juego, padx=30)  # Botón PLAY
button_play.pack(pady=10)  # Empaquetar el botón en el marco con espacio en la parte inferior
##########################################################################################################

window.mainloop() #:)
