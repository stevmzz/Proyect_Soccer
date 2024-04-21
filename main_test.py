from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.font import Font
import pygame
import os
from pygame.locals import *
######################################################################################################
#Función para cerrar las ventanas
def Cerrar_Ventana(event):
    if 'Ventana_Play' in globals() and Ventana_Play.winfo_exists():
        Ventana_Play.destroy()
    elif 'Ventana_About' in globals() and Ventana_About.winfo_exists():
        Ventana_About.destroy()
    else:
        Ventana_Principal.destroy()
######################################################################################################
#Ventanas Secundarias
def Abrir_Ventana_Play():
    global Ventana_Play
    Ventana_Play = tk.Toplevel()
    Ventana_Play.attributes('-fullscreen', True)
    Ventana_Play.title("PLAY")
    Ventana_Play.config(bg="black")
    Ventana_Play.bind('<Escape>', Cerrar_Ventana)

    Canvas_Jugador1 = tk.Canvas(Ventana_Play, width=300, height=300, bg="white")
    Canvas_Jugador1.pack(side="left")

    Canvas_Jugador2 = tk.Canvas(Ventana_Play, width=300, height=300, bg="white")
    Canvas_Jugador2.pack(side="left")

    messi = Image.open("images/Jugadores/messi.png")
    messi = messi.resize((300, 300), Image.LANCZOS)
    messi_tk = ImageTk.PhotoImage(messi)
    Canvas_Jugador1.create_image(0, 0, anchor="nw", image=messi_tk)
    Canvas_Jugador1.image = messi_tk

    haaland = Image.open("images/Jugadores/haaland.png")
    haaland = haaland.resize((300, 300), Image.LANCZOS)
    haaland_tk = ImageTk.PhotoImage(haaland)
    Canvas_Jugador2.create_image(0, 0, anchor="nw", image=haaland_tk)
    Canvas_Jugador2.image = haaland_tk

def Mostrar_Frame_Creador1():
    Frame_Creador2.place_forget()
    Frame_Creador1.place(x=0, y=0, relwidth=0.5, relheight=1)

def Mostrar_Frame_Creador2():
    Frame_Creador1.place_forget()
    Frame_Creador2.place(x=0, y=0, relwidth=0.5, relheight=1)
    Frame_Creador.place_forget()

def Abrir_Ventana_About():
    global Ventana_About, Font_Label
    Ventana_About = tk.Toplevel()
    Ventana_About.attributes('-fullscreen', True)
    Ventana_About.title("ABOUT")
    Ventana_About.config(bg="black")
    Ventana_About.bind('<Escape>', Cerrar_Ventana)
###################################################
    Canvas_Superior = tk.Canvas(Ventana_About, bg="white", width=1366, height=256, highlightthickness=0)
    Canvas_Superior.pack(side="top")

    Canvas_Creador2 = tk.Canvas(Canvas_Superior, bg="grey", width=683, height=256, highlightthickness=0)
    Canvas_Creador2.pack(side="left")

    Canvas_Creador1 = tk.Canvas(Canvas_Superior, bg="black", width=683, height=256, highlightthickness=0)
    Canvas_Creador1.pack(side="left")

    Label_Creador1 = tk.Label(Canvas_Creador1, text="Steven Aguilar Alvarez\n3 0557 0029\n2028 2024 65", fg="white", bg="black", font=Font_Label)
    Label_Creador1.place(relx=0.5, rely=0.1, anchor='center', y=95)

    Label_Creador2 = tk.Label(Canvas_Creador2, text="Jannes Ronhaar Flores\n3 0557 0029\n2028 2024 65", fg="black", bg="grey", font=Font_Label)
    Label_Creador2.place(relx=0.5, rely=0.1, anchor='center', y=95)
###################################################
    Canvas_Inferior = tk.Canvas(Ventana_About, bg="white", width=1366, height=512, highlightthickness=0)
    Canvas_Inferior.pack(side="top")

    Label_Info1 = tk.Label(Canvas_Inferior, text="FUNDAMENTOS DE SISTEMAS COMPUTACIONALES\nLICENCIATURA EN INGENIERÍA EN COMPUTADORES\n2024\nLUIS ALBERTO CHAVARRÍA\nCOSTA RICA\nVERSION 0.1", font=Font_Label, fg="black", bg="white")
    Label_Info1.place(relx=0.5, rely=0.1, anchor='center', y=120)
######################################################################################################
#Ventana Principal
Ventana_Principal = tk.Tk()
Ventana_Principal.attributes('-fullscreen', True)
Ventana_Principal.title("MAIN")
Ventana_Principal.bind('<Escape>', Cerrar_Ventana)
######################################################################################################
#Fuentes
Font_Button = Font(family="Courier New", size=24, weight="bold")
Font_Label = Font(family="Courier New", size=24, weight="bold")
######################################################################################################
#Fondo
def cargarImagen(nombre, width, height): 
    ruta = os.path.join('images', nombre)
    imagen = Image.open(ruta)
    imagen = imagen.resize((width, height), resample=Image.LANCZOS)
    return ImageTk.PhotoImage(imagen)

def actualizarImagen(event):
    global imagen1
    width = event.width
    height = event.height
    imagen1 = cargarImagen("wallpaper4.png", width, height)
    LabelFondo.config(image=imagen1)

imagen1 = cargarImagen("wallpaper4.png", Ventana_Principal.winfo_width(), Ventana_Principal.winfo_height())
LabelFondo = Label(Ventana_Principal, image=imagen1)
LabelFondo.place(x=0, y=0, relwidth=1, relheight=1)
Ventana_Principal.bind("<Configure>", actualizarImagen)
######################################################################################################
#Botones
Boton_Play = tk.Button(Ventana_Principal, text="PLAY", font=Font_Button, command=Abrir_Ventana_Play)
Boton_Play.pack(pady=(500,0))

Boton_About = tk.Button(Ventana_Principal, text="ABOUT", font=Font_Button, command=Abrir_Ventana_About)
Boton_About.pack(pady=10)
######################################################################################################
Label_Version = Label(Ventana_Principal,text="version: 0.1", font=("Courier New", 10, "bold"), fg="white", bg="black")
Label_Version.place(x=0, y=0)
######################################################################################################
#Música de fondo
pygame.init()
"""pygame.mixer.music.load('sounds/EA SPORTS FIFA 98 Road to World Cup - Intro.mp3')
pygame.mixer.music.play(-1)"""
######################################################################################################

Ventana_Principal.mainloop()
pygame.quit()
