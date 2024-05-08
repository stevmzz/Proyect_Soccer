from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.font import Font
import os
import pygame
import random
import time
########################################################################################
#Música
pygame.init()
pygame.mixer.music.load("sounds/EA SPORTS FIFA 98 Road to World Cup - Intro.mp3")
pygame.mixer.music.play(-1)
########################################################################################
def Cerrar_Ventana(event):
    if 'Ventana_Play' in globals() and Ventana_Play.winfo_exists():
        Ventana_Play.destroy()
    elif 'Ventana_About' in globals() and Ventana_About.winfo_exists():
        Ventana_About.destroy()
    elif 'Ventana_Ranking' in globals() and Ventana_Ranking.winfo_exists():
        Ventana_Ranking.destroy()
    elif 'Ventana_Juego' in globals() and Ventana_Juego.winfo_exists():
        Ventana_Juego.destroy()
    else:
        Ventana_Principal.destroy()
########################################################################################
def Cambiar_Imagen_Carrusel_Jugadores():
    global imagen_index_jugadores, team_index
    if 'imagen_index_jugadores' not in globals():
        imagen_index_jugadores = 0 
    if imagen_index_jugadores == len(equipos[team_index]) - 1:
        imagen_index_jugadores = 0
    else:
        imagen_index_jugadores += 1

    imagen_actual = equipos[team_index][imagen_index_jugadores]
    canvas_imagen_jugadores.itemconfig(imagen_canvas_jugadores, image=imagen_actual)
########################################################################################
def Cambiar_Equipo_Jugador1():
    global team_index_jugador1
    if team_index_jugador1 == len(equipos) - 1:
        team_index_jugador1 = 0
    else:
        team_index_jugador1 += 1

    nombre_equipo_jugador1.set(nombres_equipos[team_index_jugador1])
    imagen_actual_jugador1 = equipos[team_index_jugador1][imagen_index_jugadores]
    canvas_imagen_jugador1.itemconfig(imagen_canvas_jugador1, image=imagen_actual_jugador1)

def Cambiar_Jugador_Jugador1():
    global jugador_index_jugador1
    if jugador_index_jugador1 == len(equipos[team_index_jugador1]) - 1:
        jugador_index_jugador1 = 0
    else:
        jugador_index_jugador1 += 1

    imagen_actual_jugador1 = equipos[team_index_jugador1][jugador_index_jugador1]
    canvas_imagen_jugador1.itemconfig(imagen_canvas_jugador1, image=imagen_actual_jugador1)

def Cambiar_Equipo_Jugador2():
    global team_index_jugador2
    if team_index_jugador2 == len(equipos) - 1:
        team_index_jugador2 = 0
    else:
        team_index_jugador2 += 1

    nombre_equipo_jugador2.set(nombres_equipos[team_index_jugador2])
    imagen_actual_jugador2 = equipos[team_index_jugador2][imagen_index_jugadores]
    canvas_imagen_jugador2.itemconfig(imagen_canvas_jugador2, image=imagen_actual_jugador2)

def Cambiar_Jugador_Jugador2():
    global jugador_index_jugador2
    if jugador_index_jugador2 == len(equipos[team_index_jugador2]) - 1:
        jugador_index_jugador2 = 0
    else:
        jugador_index_jugador2 += 1

    imagen_actual_jugador2 = equipos[team_index_jugador2][jugador_index_jugador2]
    canvas_imagen_jugador2.itemconfig(imagen_canvas_jugador2, image=imagen_actual_jugador2)
########################################################################################
def Abrir_Ventana_Play():
    global Ventana_Play, imagen_canvas_jugadores, canvas_imagen_jugadores, canvas_imagen_jugador1, imagen_canvas_jugador1, canvas_imagen_jugador2, imagen_canvas_jugador2, equipos, imagen_index_jugadores, nombres_equipos, team_index_jugador1, team_index_jugador2, jugador_index_jugador1, jugador_index_jugador2
    Ventana_Play = tk.Toplevel()
    Ventana_Play.attributes('-fullscreen', True)
    Ventana_Play.config(bg="black")
    Ventana_Play.title("PLAY")
    Ventana_Play.bind('<Escape>', Cerrar_Ventana)

    equipos = [
        [
            ImageTk.PhotoImage(Image.open("Jugadores/Equipo1/jugador1.png").resize((300, 300), Image.LANCZOS)),
            ImageTk.PhotoImage(Image.open("Jugadores/Equipo1/jugador2.png").resize((300, 300), Image.LANCZOS)),
            ImageTk.PhotoImage(Image.open("Jugadores/Equipo1/jugador3.png").resize((300, 300), Image.LANCZOS)),
        ],
        [
            ImageTk.PhotoImage(Image.open("Jugadores/Equipo2/jugador1.png").resize((300, 300), Image.LANCZOS)),
            ImageTk.PhotoImage(Image.open("Jugadores/Equipo2/jugador2.png").resize((300, 300), Image.LANCZOS)),
            ImageTk.PhotoImage(Image.open("Jugadores/Equipo2/jugador3.png").resize((300, 300), Image.LANCZOS)),
        ],
        [
            ImageTk.PhotoImage(Image.open("Jugadores/Equipo3/jugador1.png").resize((300, 300), Image.LANCZOS)),
            ImageTk.PhotoImage(Image.open("Jugadores/Equipo3/jugador2.png").resize((300, 300), Image.LANCZOS)),
            ImageTk.PhotoImage(Image.open("Jugadores/Equipo3/jugador3.png").resize((300, 300), Image.LANCZOS)),
        ],
    ]

    nombres_equipos = ["MCI", "PSG", "RMA"]

    global imagen_index_jugadores, team_index_jugador1, team_index_jugador2, jugador_index_jugador1, jugador_index_jugador2
    imagen_index_jugadores = 0
    team_index_jugador1 = 0
    team_index_jugador2 = 0
    jugador_index_jugador1 = 0
    jugador_index_jugador2 = 0

    global nombre_equipo_jugador1
    nombre_equipo_jugador1 = tk.StringVar()
    nombre_equipo_jugador1.set(nombres_equipos[team_index_jugador1])
    label_nombre_equipo_jugador1 = tk.Label(Ventana_Play, textvariable=nombre_equipo_jugador1, font=Font_Label, fg="white", bg="black")
    label_nombre_equipo_jugador1.place(x=450,y=50)

    imagen_actual_jugador1 = equipos[team_index_jugador1][imagen_index_jugadores]
    global canvas_imagen_jugador1, imagen_canvas_jugador1
    canvas_imagen_jugador1 = tk.Canvas(Ventana_Play, width=300, height=300, bg="white")
    imagen_canvas_jugador1 = canvas_imagen_jugador1.create_image(0, 0, anchor=tk.NW, image=imagen_actual_jugador1)
    canvas_imagen_jugador1.place(x=330, y=150)
    global Font_Button_Ready

    Font_Button_Seleccion = Font(family="helvatica", size=18, weight="bold")
    Font_Button_Ready = Font(family="helvatica", size=20, weight="bold")
    
    boton_carrusel_jugador1 = tk.Button(Ventana_Play, font=Font_Button_Seleccion,text="NEXT PLAYER", command=Cambiar_Jugador_Jugador1, width=16)
    boton_carrusel_jugador1.place(x=365, y=540)

    boton_cambiar_equipo_jugador1 = tk.Button(Ventana_Play, font=Font_Button_Seleccion, text="NEXT TEAM", command=Cambiar_Equipo_Jugador1, width=16)
    boton_cambiar_equipo_jugador1.place(x=365, y=600)

    global nombre_equipo_jugador2
    nombre_equipo_jugador2 = tk.StringVar()
    nombre_equipo_jugador2.set(nombres_equipos[team_index_jugador2])
    label_nombre_equipo_jugador2 = tk.Label(Ventana_Play, textvariable=nombre_equipo_jugador2, font=Font_Label, fg="white", bg="black")
    label_nombre_equipo_jugador2.place(x=850, y=50)

    # Configurar carrusel de jugador 2
    imagen_actual_jugador2 = equipos[team_index_jugador2][imagen_index_jugadores]
    global canvas_imagen_jugador2, imagen_canvas_jugador2
    canvas_imagen_jugador2 = tk.Canvas(Ventana_Play, width=300, height=300, bg="white")
    imagen_canvas_jugador2 = canvas_imagen_jugador2.create_image(0, 0, anchor=tk.NW, image=imagen_actual_jugador2)
    canvas_imagen_jugador2.place(x=730, y=150)

    boton_carrusel_jugador2 = tk.Button(Ventana_Play, font=Font_Button_Seleccion, text="NEXT PLAYER", command=Cambiar_Jugador_Jugador2, width=16)
    boton_carrusel_jugador2.place(x=765, y=540)

    # Configurar botón para cambiar de equipo jugador 2
    boton_cambiar_equipo_jugador2 = tk.Button(Ventana_Play, font=Font_Button_Seleccion, text="NEXT TEAM", command=Cambiar_Equipo_Jugador2, width=16)
    boton_cambiar_equipo_jugador2.place(x=765, y=600)
    global boton_listo_jugador1, boton_listo_jugador2
    
    boton_listo_jugador1 = tk.Button(Ventana_Play, font=Font_Button_Ready, text="READY", command=Ready1, width=17)
    boton_listo_jugador1.place(x=340, y=660)

    boton_listo_jugador2 = tk.Button(Ventana_Play, font=Font_Button_Ready, text="READY", command=Ready2, width=17)
    boton_listo_jugador2.place(x=740, y=660)

    Label_Equipo_1 = tk.Label(Ventana_Play, font=Font_Button_Ready, text="PLAYER #1", fg="white", bg="black")
    Label_Equipo_1.place(x=400, y=480)

    Label_Equipo_2 = tk.Label(Ventana_Play, font=Font_Button_Ready, text="PLAYER #2", fg="white", bg="black")
    Label_Equipo_2.place(x=800, y=480)
########################################################################################
def Ready1():
    if boton_listo_jugador1["text"] == "READY":
        boton_listo_jugador1.config(text="!READY¡")
        Abrir_Real()
def Ready2():
    if boton_listo_jugador2["text"] == "READY":
        boton_listo_jugador2.config(text="!READY¡")
        Abrir_Real()
def Abrir_Real():
    if boton_listo_jugador1["text"] == "!READY¡" and boton_listo_jugador2["text"] == "!READY¡":
        Abrir_Ventana_Juego_Real()
########################################################################################
def Abrir_Ventana_Juego_Real():
    global frame_index1, resultado1, Ventana_Juego

    def cargar_frames():
        global frame_index1
        frames = []
        for i in range(1, 12):
            ruta = os.path.join(f'images/Frames_Coin/{i}.png')
            imagen = Image.open(ruta)
            frames.append(ImageTk.PhotoImage(imagen.resize((200, 200), Image.LANCZOS)))
        return frames

    def animar_moneda():
        global frame_index1, resultado1, resultado

        canvas.itemconfig(imagen_moneda, image=frames[frame_index1])

        frame_index1 = (frame_index1 + 1) % len(frames)
        if frame_index1 == 0:
            resultado1 = random.choice(["PLAYER #2", "PLAYER #1"])
            resultado_label.config(text=f"LOCAL TEAM: {resultado1}")
            canvas.itemconfig(imagen_moneda, image=frames[0] if resultado1 == "Cara" else frames[6])
        else:
            Ventana_Juego.after(100, animar_moneda)

    frames = cargar_frames()

    Ventana_Juego = tk.Toplevel(Ventana_Play)
    Ventana_Juego.attributes('-fullscreen', True)
    Ventana_Juego.title("JUEGO")
    Ventana_Juego.config(bg="black")

    canvas = tk.Canvas(Ventana_Juego, width=400, height=200, bg="black", highlightthickness=0)
    canvas.pack(pady=50)
    imagen_moneda = canvas.create_image(200, 100, image=None)

    resultado_label = tk.Label(Ventana_Juego, text="LOCAL TEAM: ", font=("helvetica", 18), fg="white", bg="black")
    resultado_label.pack()

    Boton_Play = tk.Button(Ventana_Juego, font=Font_Button_Ready, text="PLAY", fg="white", bg="black", width=10, height=3, command=Abrir_Playing)
    Boton_Play.place(x=600, y=480)

    frame_index1 = 0
    animar_moneda()

def Abrir_Playing():
    global Ventana_Playing, resultado1
    Ventana_Playing = tk.Toplevel()
    Ventana_Playing.attributes('-fullscreen', True)
    Ventana_Playing.config(bg="black")
    Ventana_Playing.title("PLAYING")
    Ventana_Playing.bind('<Escape>', Cerrar_Ventana)

########################################################################################
def Abrir_Ventana_About():
    global Ventana_About, Font_Label
    Ventana_About = tk.Toplevel()
    Ventana_About.attributes('-fullscreen', True)
    Ventana_About.title("ABOUT")
    Ventana_About.config(bg="black")
    Ventana_About.bind('<Escape>', Cerrar_Ventana)

    Label_Version = Label(Ventana_About, text="ABOUT", font=("helvatica", 20, "bold"), fg="white", bg="black")
    Label_Version.pack(pady=20)

    Canvas_Controles = tk.Canvas(Ventana_About, background="white", width=678, height=768)
    Canvas_Controles.pack(side="left")

    Rules_Label = tk.Label(Canvas_Controles, text="RULES", font=("helvatica", 20, "bold"), fg="black", bg="white")
    Rules_Label.place(x=290, y=15)

    Rules = tk.Label(Canvas_Controles, text="PENALTY MAN ES UN EMOCIONANTE JUEGO \n DE TIROS PENALES DONDE DOS JUGADORES COMPITEN \n PARA DEMOSTRAR SU HABILIDAD COMO ARTILLEROS \n Y PORTEROS. CADA JUGADOR SELECCIONARÁ UN EQUIPO Y \n UN JUGADOR ESTRELLA PARA ENFRENTARSE EN UNA REÑIDA \n COMPETENCIA DE CINCO TIROS PENALES ALTERNADOS.", font=("helvatica", 15, "bold"), fg="black", bg="white")
    Rules.place(x=25, y=100)

    info_Label = tk.Label(Canvas_Controles, text="INFORMATION", font=("helvatica", 20, "bold"), fg="black", bg="white")
    info_Label.place(x=230, y=300)

    info = tk.Label(Canvas_Controles, text="TECNOLOGICO DE COSTA RICA", font=("helvatica", 17, "bold"), fg="black", bg="white")
    info.place(x=38, y=380)

    info1 = tk.Label(Canvas_Controles, text="FUNDAMENTOS DE SISTEMAS COMPUTACIONALES", font=("helvatica", 17, "bold"), fg="black", bg="white")
    info1.place(x=38, y=420)

    info2 = tk.Label(Canvas_Controles, text="COSTA RICA", font=("helvatica", 17, "bold"), fg="black", bg="white")
    info2.place(x=38, y=460)

    info3 = tk.Label(Canvas_Controles, text="2024", font=("helvatica", 17, "bold"), fg="black", bg="white")
    info3.place(x=38, y=500)

    info3 = tk.Label(Canvas_Controles, text="PROF. LUIS ALBERTO CHAVARRIA ZAMORA", font=("helvatica", 17, "bold"), fg="black", bg="white")
    info3.place(x=38, y=540)

    info3 = tk.Label(Canvas_Controles, text="VERSION: 0.1", font=("helvatica", 17, "bold"), fg="black", bg="white")
    info3.place(x=38, y=580)

    Canvas_Central = tk.Canvas(Ventana_About, background="black", width=10, height=768, highlightthickness=0)
    Canvas_Central.pack(side="left")

    Canvas_Creadores = tk.Canvas(Ventana_About, background="white", width=678, height=768)
    Canvas_Creadores.pack(side="left")

    Creadores_Label = tk.Label(Canvas_Creadores, text="PROYECT by", font=("helvatica", 20, "bold"), fg="black", bg="white")
    Creadores_Label.place(x=250, y=15)

    Creador0 = tk.Label(Canvas_Creadores, text="------", font=("helvatica", 17, "bold"), fg="black", bg="white")
    Creador0.place(x=38, y=100)

    Creador = tk.Label(Canvas_Creadores, text="STEVEN AGUILAR ALVAREZ", font=("helvatica", 17, "bold"), fg="black", bg="white")
    Creador.place(x=38, y=180)

    Creador1 = tk.Label(Canvas_Creadores, text="2024202865", font=("helvatica", 17, "bold"), fg="black", bg="white")
    Creador1.place(x=38, y=220)

    Creador0 = tk.Label(Canvas_Creadores, text="------", font=("helvatica", 17, "bold"), fg="black", bg="white")
    Creador0.place(x=38, y=280)

    Creador = tk.Label(Canvas_Creadores, text="JANNES RONHAAR FLORES", font=("helvatica", 17, "bold"), fg="black", bg="white")
    Creador.place(x=38, y=360)

    Creador1 = tk.Label(Canvas_Creadores, text="2023179878", font=("helvatica", 17, "bold"), fg="black", bg="white")
    Creador1.place(x=38, y=400)

    Creador00 = tk.Label(Canvas_Creadores, text="------", font=("helvatica", 17, "bold"), fg="black", bg="white")
    Creador00.place(x=38, y=480)
########################################################################################
def Abrir_Ventana_Ranking():
    global Ventana_Ranking
    Ventana_Ranking = tk.Toplevel()
    Ventana_Ranking.attributes('-fullscreen', True)
    Ventana_Ranking.title("Rankingd")
    Ventana_Ranking.config(bg="black")
    Ventana_Ranking.bind('<Escape>', Cerrar_Ventana)

    Title = tk.Label(Ventana_Ranking, text="GOALSCORERS", font=("helvatica", 17, "bold"), fg="black", bg="white")
    Title.place(x=38, y=38)
########################################################################################
#Ventana Principal
Ventana_Principal = tk.Tk()
Ventana_Principal.attributes('-fullscreen', True)
Ventana_Principal.title("MAIN")
Ventana_Principal.bind('<Escape>', Cerrar_Ventana)
Ventana_Principal.config(background="black")

def cargarImagen(nombre, width, height): 
    ruta = os.path.join('images', nombre)
    imagen = Image.open(ruta)
    imagen = imagen.resize((width, height), resample=Image.LANCZOS)
    return ImageTk.PhotoImage(imagen)

def actualizarImagen(event):
    global imagen1
    width = event.width
    height = event.height
    imagen1 = cargarImagen("wallpaper6.png", width, height)
    LabelFondo.config(image=imagen1)

imagen1 = cargarImagen("wallpaper6.png", Ventana_Principal.winfo_width(), Ventana_Principal.winfo_height())
LabelFondo = Label(Ventana_Principal, image=imagen1)
LabelFondo.place(x=0, y=0, relwidth=1, relheight=1)
Ventana_Principal.bind("<Configure>", actualizarImagen)
########################################################################################
Font_Button = Font(family="helvatica", size=30, weight="bold")
Font_Label = Font(family="helvatica", size=24, weight="bold")
########################################################################################
# Botones
Boton_About = tk.Button(Ventana_Principal, text="ABOUT", font=Font_Button, command=Abrir_Ventana_About, fg="black", bg="white", padx=38, borderwidth=0, activebackground="black", activeforeground="white", width=8)
Boton_About.place(x=190, y=220)

Boton_Play = tk.Button(Ventana_Principal, text="PLAY", font=Font_Button, command=Abrir_Ventana_Play, fg="white", bg="black", padx=50, highlightthickness=1, width=9, height=2)
Boton_Play.place(x=167, y=326)

Boton_Ranking = tk.Button(Ventana_Principal, text="RANKING", font=Font_Button, command=Abrir_Ventana_Ranking, fg="black", bg="white", padx=38, borderwidth=0, activebackground="black", activeforeground="white", width=8)
Boton_Ranking.place(x=190, y=480)

Label_Version = Label(Ventana_Principal, text="version: 0.1", font=("helvatica", 12, "bold"), fg="white", bg="black")
Label_Version.place(x=10, y=10)
########################################################################################

Ventana_Principal.mainloop()
