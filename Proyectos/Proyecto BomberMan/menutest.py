from tkinter import * # Tkinter
import tkinter as tk # Tkinter
from PIL import Image, ImageTk # Imágenes
from tkinter.font import Font # Fuentes
import pygame # Música
import os # Obtener ruta del fondo
import subprocess # Abrir otros .py
import csv # Ranking
import cv2 # video
##########################################################################################################
#Fondo
def cargarImagen(nombre, ancho, alto):  # Cargar imagen y ajustar tamaño
    ruta = os.path.join('images/wallpaper', nombre)  # Obtener la ruta completa de la imagen
    imagen = Image.open(ruta)  # Abrir la imagen
    imagen = imagen.resize((ancho, alto), resample=Image.LANCZOS)  # Redimensionar la imagen
    return ImageTk.PhotoImage(imagen)  # Devolver la imagen

def actualizarImagen(event):  # Actualizar imagen en respuesta a un evento
    global imagen1  # Declarar variable global
    ancho = event.width  # Obtener ancho del evento
    alto = event.height  # Obtener alto del evento
    imagen1 = cargarImagen("fondo.png", ancho, alto)  # Cargar imagen con nuevo tamaño
    LabelFondo.config(image=imagen1)  # Mostrar imagen actualizada
##########################################################################################################
#Selección de personaje
def iniciar_juego(): # Iniciar Juego
    proceso = subprocess.Popen(["python", "home.py"]) # Abre el .py
    proceso.wait()  # Esperar a que el proceso termine
    if pygame.mixer.music.get_busy():  # Verificar si hay música en reproducción
        pygame.mixer.music.set_volume(0)  # Silenciar la música del juego
##########################################################################################################
#Ventana Options
def abrir_ventana_options(): # Abrir ventana options
    global ventana_options, boton_mute_unmute # global de ventana options
    ventana_options = tk.Toplevel(ventana_principal, bg="black") # Toplevel de la ventana
    ventana_options.title("OPTIONS") # Título
    ventana_options.attributes('-fullscreen', True) # Pantalla completa
    Funte_Options_Main = Font(family="Courier New", size=20, weight="bold") # Fuente del título

    label_volumen = Label(ventana_options, font=Funte_Options_Main, text="MUTE GAME", fg="white", bg="black") # Label del texto
    label_volumen.pack(pady=10) # Pack del label
    
    boton_mute_unmute = tk.Button(ventana_options, text="Mute", fg="white", bg="black", borderwidth=2, relief="solid", command=silenciar) # Botón de silenciar
    boton_mute_unmute.pack(pady=5) # Pack del botón

def silenciar():
    if pygame.mixer.music.get_volume() == 0:    # Verificar si la música está silenciada
        pygame.mixer.music.set_volume(1)  # Desactivar el silencio
        with open("mute_state.txt", "w") as file: # Escribir en el archivo
            file.write("0")  # Guardar el estado (0: no silenciado) en el archivo
        boton_mute_unmute.config(text="Mute")  # Actualizar el texto del botón a "Silenciar"
    else:
        pygame.mixer.music.set_volume(0)  # Silenciar la música
        with open("mute_state.txt", "w") as file: # Escribir en el archivo
            file.write("1")  # Guardar el estado (1: silenciado) en el archivo
        boton_mute_unmute.config(text="Unmute")  # Actualizar el texto del botón a "Desilenciar"

    ventana_options.bind('<Escape>', close_window) #Cerrar ventana
##########################################################################################################
#Ventana información
def abrir_ventana_info(): # Abrir la ventana info
    global ventana_info # global de la ventana
    ventana_info = tk.Toplevel(ventana_principal, bg="BLACK") # Toplevel de la ventana
    ventana_info.title("INFO") # Título
    ventana_info.attributes('-fullscreen', True) # Pantalla completa
    contenedor_principal = tk.Frame(ventana_info) # Frame principal
    contenedor_principal.pack(fill="both", expand=True) # Pack del frame

    contenedor_izquierdo = tk.Frame(contenedor_principal, bg="white") # Frame izquierdo
    contenedor_izquierdo.pack(side="left", fill="both", expand=True) # Pack del frame

    contenedor_derecho = tk.Frame(contenedor_principal, bg="black") #Frame derecho
    contenedor_derecho.pack(side="left", fill="both", expand=True) # Pack del frame

    Font_Titulo = Font(family="Courier New", size=24, weight="bold") # Fuente del título
    Font_SubTitulo = Font(family="Courier New", size=20, weight="bold") # Fuente de subtítulo

    label_info = Label(contenedor_izquierdo, text="CONTROLES\n", font=Font_Titulo, fg="black", bg="white") # Título controles
    label_info.pack(pady=20) # Pack del título

    label_info = Label(contenedor_izquierdo, text="LEFT --- A , 🡸\nRIGHT --- D , 🡺\nUP --- W , 🡹\nDOWN --- S , 🡻\nBOMB --- space\nEXIT --- esc\nGET KEY --- J\nOPEN DOOR --- K", font=Font_SubTitulo, fg="black", bg="white") # Controles
    label_info.pack(pady=10) # Pack de los controles

    label_info = Label(contenedor_derecho, text="INFORMACIÓN DEL CREADOR", font=Font_Titulo, fg="white", bg="black") # Título de información del creador
    label_info.pack(pady=(20,10)) # Pack del título

    label_info = Label(contenedor_derecho, text="STEVEN AGUILAR ALVAREZ \n 3 0557 0029 \n INTRODUCCIÓN A LA PROGRAMACIÓN \n LICENCIATURA EN INGENIERÍA EN COMPUTADORES", font=Font_SubTitulo, fg="white", bg="black") # Información
    label_info.pack() # Pack de información

    label_info = Label(contenedor_derecho, text="INFORMACIÓN", font=Font_Titulo, fg="white", bg="black") # Título de información
    label_info.pack(pady=(70,10)) # Pack del título

    label_info = Label(contenedor_derecho, text="2024 \n JASON LEITÓN JIMÉNEZ \n COSTA RICA \n BOMBERMAN by steven 0.1", font=Font_SubTitulo, fg="white", bg="black") # Información
    label_info.pack() # Pack de inforación
    ventana_info.bind('<Escape>', close_window) # Cerrar Ventana
##########################################################################################################
#Ranking
def obtener_ranking(file_path='partidas.csv'):# Función para obtener y mostrar el ranking de jugadores
    def helper(file, ranking_dic=None): # Función auxiliar para procesar el archivo y obtener el ranking
        if ranking_dic is None: # Inicializar el diccionario de ranking si es None
            ranking_dic = {}
        line = file.readline() # Leer una línea del archivo
        if not line: # Si no hay más líneas, ordenar el ranking y devolver los primeros 5 jugadores
            ranking = sorted(ranking_dic.items(), key=lambda x: x[1], reverse=True) # Ordenar el diccionario en orden descendente
            return ranking[:5] # Devolver los primeros 5 elementos del ranking, que son los jugadores con más puntos

        row = line.strip().split(',') # Eliminar espacios en blanco y dividir en una lista usando la coma
        nombre = row[0] # Obtener el nombre del jugador de la primera posición de la lista
        puntos = int(row[1]) # Obtener los puntos del jugador de la segunda posición de la lista, convirtiéndolos a un entero

        if nombre not in ranking_dic or puntos > ranking_dic[nombre]: # Verificar si el jugador no está en el ranking o tiene más puntos
            ranking_dic[nombre] = puntos # Si es así, actualizar su puntaje en el diccionario de ranking
        return helper(file, ranking_dic) # Actualizar ranking del archivo

    with open(file_path, mode='r') as file: # Abrir el archivo en modo lectura y llamar a la función auxiliar
        return helper(file)  # Devolver el ranking obtenido

def obtener_nombre_jugador(): # Función para obtener el nombre del jugador desde un archivo
    with open('nombre_jugador.txt', 'r') as file: #Leer el nombre
        return file.read()  # Devolver el nombre del jugador leído del archivo

def obtener_puntos_totales(): # Función para obtener los puntos totales desde un archivo
    with open('puntos.txt', 'r') as file: # Leer los puntos
        return file.read()  # Devolver los puntos totales leídos del archivo

def mostrar_ranking(ranking_data, window, index=1):# Función para mostrar el ranking en una ventana
    Font_Ranked = Font(family="Courier New", size=15, weight="bold") # Fuente para los elementos del ranking

    if index > 5: # Mostrar solo los primeros 5
        return
    jugador = ranking_data[index - 1] # Obtener datos del jugador en el índice actual del ranking
    etiqueta_jugador = tk.Label(window, text=f"{index}. {jugador[0]} - Puntos: {jugador[1]}", font=Font_Ranked, bg="black", fg="white", pady=20) # Label para mostrar al jugador y sus puntos
    etiqueta_jugador.pack(side="top")  # 
    mostrar_ranking(ranking_data, window, index + 1) # Llamar recursivamente para mostrar el siguiente jugador del ranking

def abrir_ventana_ranking(): # Función para abrir la ventana de ranking
    global ventana_ranking  # Ventana de ranking global
    ventana_ranking = tk.Toplevel(ventana_principal)  # Crear ventana de ranking como una ventana de nivel superior
    ventana_ranking.title("RANKING")  # Establecer el título de la ventana como "RANKING"
    ventana_ranking.attributes('-fullscreen', True)  # Configurar la ventana para pantalla completa
    ventana_ranking.config(bg="black")  # Establecer fondo negro para la ventana

    def guardar_ranking(nombre_jugador, puntos_jugador): # Función para guardar el ranking actualizado
        with open('partidas.csv', mode='a', newline='') as file: # Abre el archivo en append y no crea lineas nuevas
            writer = csv.writer(file) # Escribe en archivo
            writer.writerow([nombre_jugador, str(puntos_jugador)])  # Escribir nombre y puntos en el archivo en una fila

    puntos_jugador = obtener_puntos_totales() # Obtener puntos
    nombre_jugador = obtener_nombre_jugador() # Obtener nombre del jugador
    guardar_ranking(nombre_jugador, puntos_jugador) # Guardar el nombre y puntos en el archivo

    Font_Ranking = Font(family="Courier New", size=20, weight="bold") # Fuente del ranking

    label_Ranking = Label(ventana_ranking, font=Font_Ranking, text="MEJORES JUGADORES", fg="white", bg="black") # Título
    label_Ranking.pack(side="top", pady=(30))  # Pack del título
    
    ranking = obtener_ranking() # Obtener y mostrar el ranking
    mostrar_ranking(ranking, ventana_ranking)  # Llamar a la función para mostrar el ranking en la ventana
    
    ventana_ranking.bind('<Escape>', close_window)  # Asociar la tecla Escape con la función para cerrar la ventana
##########################################################################################################
#Ventana Lore
def abrir_ventana_lore(): # Abrir la ventana
    global ventana_lore  # Ventana global para la historia
    ventana_lore = tk.Toplevel(ventana_principal, bg="black")  # Ventana emergente negra
    ventana_lore.title("STORY")  # Título de la ventana
    ventana_lore.attributes('-fullscreen', True)  # Pantalla completa

    reproducir_video(ventana_lore, ruta_video, width=1024, height=768)  # Video en la ventana
    reproducir_audio(ruta_audio)  # Audio relacionado

    ventana_lore.bind('<Escape>', close_window)  # Cerrar con Escape
##########################################################################################################
#Ventana Principal
ventana_principal = tk.Tk()  # Ventana principal
ventana_principal.attributes('-fullscreen', True)  # Pantalla completa
ventana_principal.title("BOMBERMAN")  # Título: "BOMBERMAN"
ventana_principal.configure(bg='black')  # Fondo negro

pygame.mixer.init()  # Inicializar mezclador de sonido
pygame.mixer.music.load('sounds/scizzie_aquatic_ambience.mp3')  # Cargar música
pygame.mixer.music.play(-1)  # Reproducir en bucle

imagen1 = cargarImagen("fondo.png", ventana_principal.winfo_width(), ventana_principal.winfo_height())  # Cargar imagen de fondo
LabelFondo = Label(ventana_principal, image=imagen1)  # Etiqueta de imagen de fondo
LabelFondo.place(x=0, y=0, relwidth=1, relheight=1)  # Ubicar la imagen en la ventana

ventana_principal.bind("<Configure>", actualizarImagen)  # Actualizar imagen al cambiar tamaño de ventana

label_version = Label(ventana_principal,text="version: 0.1", font=("Courier New", 10, "bold"), fg="white", bg="black")  # Etiqueta de versión
label_version.pack(side="left", anchor="nw", pady=5, padx=5)  # Posicionar etiqueta
##########################################################################################################
#Cerrar la ventana
def close_window(event):
    if 'ventana_options' in globals() and ventana_options.winfo_exists():  # Si la ventana de opciones existe, destrúyela
        ventana_options.destroy()
    elif 'ventana_ranking' in globals() and ventana_ranking.winfo_exists():  # Si la ventana de ranking existe, destrúyela
        ventana_ranking.destroy()
    elif 'ventana_info' in globals() and ventana_info.winfo_exists():  # Si la ventana de información existe, destrúyela
        ventana_info.destroy()
    elif 'ventana_lore' in globals() and ventana_lore.winfo_exists():  # Si la ventana de historia existe, destrúyela
        ventana_lore.destroy()  # Destruir la ventana de historia
        pygame.mixer.music.stop()  # Detener la reproducción del audio
        pygame.mixer.music.load('sounds/scizzie_aquatic_ambience.mp3')  # Cargar música para la ventana principal
        pygame.mixer.music.play(-1)  # Reproducir en bucle
        pygame.mixer.music.set_volume(1)  # Establecer volumen al máximo
    else:
        ventana_principal.destroy()  # Si ninguna ventana anterior existe, destruir la ventana principal

ventana_principal.bind('<Escape>', close_window)  # Enlazar la tecla 'Escape' para llamar a la función close_window
##########################################################################################################
#Botones
font_button = Font(family="Courier New", size=20, weight="bold")  # Fuente para los botones.

boton_play = tk.Button(ventana_principal, font=font_button, text="PLAY", fg="white", bg="black", borderwidth=2, relief="solid", command=iniciar_juego)  # Botón PLAY.
boton_play.pack(pady=5)  # Empaquetar el botón con relleno vertical.

boton_options = tk.Button(ventana_principal, font=font_button, text="OPTIONS", fg="white", bg="black", borderwidth=2, relief="solid", command=abrir_ventana_options)  # Botón OPTIONS.
boton_options.pack(pady=5)  # Empaquetar el botón con relleno vertical.

boton_info = tk.Button(ventana_principal, font=font_button, text="INFORMATION", fg="white", bg="black", borderwidth=2, relief="solid", command=abrir_ventana_info)  # Botón INFORMATION.
boton_info.pack(pady=5)  # Empaquetar el botón con relleno vertical.

boton_ranking = tk.Button(ventana_principal, font=font_button, text="RANKING", fg="white", bg="black", borderwidth=2, relief="solid", command=abrir_ventana_ranking)  # Botón RANKING.
boton_ranking.pack(pady=5)  # Empaquetar el botón con relleno vertical.

boton_historia = tk.Button(ventana_principal, font=font_button, text="STORY", fg="white", bg="black", borderwidth=2, relief="solid", command=abrir_ventana_lore)  # Botón STORY.
boton_historia.pack(pady=5)  # Empaquetar el botón con relleno vertical.

boton_play.place(relx=0.75, rely=0.57, anchor=tk.CENTER)  # Posicionar el botón PLAY.
boton_options.place(relx=0.75, rely=0.64, anchor=tk.CENTER)  # Posicionar el botón OPTIONS.
boton_info.place(relx=0.75, rely=0.71, anchor=tk.CENTER)  # Posicionar el botón INFORMATION.
boton_ranking.place(relx=0.75, rely=0.78, anchor=tk.CENTER)  # Posicionar el botón RANKING.
boton_historia.place(relx=0.75, rely=0.85, anchor=tk.CENTER)  # Posicionar el botón STORY.
##########################################################################################################
#Reproducción de video
def reproducir_video(ventana, ruta_video, width=1024, height=768):  # Función para reproducir video
    cap = cv2.VideoCapture(ruta_video)  # Capturar video desde la ruta especificada
    def mostrar_cuadro():  # Función interna para mostrar cada cuadro del video
        ret, frame = cap.read()  # Leer un cuadro del video
        if ret:  # Si se lee correctamente un cuadro
            img = cv2.resize(frame, (width, height))  # Redimensionar el cuadro al tamaño deseado
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convertir el cuadro a formato RGB
            img = Image.fromarray(img)  # Crear imagen a partir del cuadro
            img = ImageTk.PhotoImage(image=img)  # Crear objeto de imagen tkinter
            label_video.configure(image=img)  # Configurar la etiqueta de video con la imagen
            label_video.image = img  # Actualizar la imagen en la etiqueta
            ventana.after(10, mostrar_cuadro)  # Llamar a la función para mostrar el siguiente cuadro después de 10 ms
        else:  # Si no se puede leer más cuadros
            cap.release()  # Liberar el objeto de captura de video
            ventana.quit()  # Salir de la ventana actual
            ventana_principal.deiconify()  # Mostrar la ventana principal

    label_video = tk.Label(ventana)  # Crear etiqueta para mostrar el video
    label_video.pack()  # Empaquetar la etiqueta en la ventana
    mostrar_cuadro()  # Llamar a la función para iniciar la reproducción del video

def reproducir_audio(ruta_audio):  # Función para reproducir audio
    pygame.mixer.init()  # Inicializar el mezclador de audio de pygame
    pygame.mixer.music.load(ruta_audio)  # Cargar el archivo de audio desde la ruta especificada
    pygame.mixer.music.play(-1)  # Reproducir el audio en bucle

ruta_video = "sounds/story.mp4"  # Ruta del archivo de video
ruta_audio = "sounds/story-audio.mp3"  # Ruta del archivo de audio
##########################################################################################################

ventana_principal.mainloop() #:)
