import tkinter as tk
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import PhotoImage
import pygame
from pygame.locals import *
import random
import time
######################################################################################################
#
#idaowdmawodmawdkm
#
#
######################################################################################################
#Ventana Principal
######################################################################################################
pygame.init()
Ventana_Principal = tk.Tk()
Ventana_Principal.attributes('-fullscreen', True)
Ventana_Principal.title("fundamentos")
######################################################################################################
#Canción de Fondo
pygame.mixer.music.load('sounds/EA SPORTS FIFA 98 Road to World Cup - Intro.mp3')
pygame.mixer.music.play(-1)
######################################################################################################
#Funciones para mostrar los frames
def Mostrar_Frame_Play():
    Frame_Play.place(x=0, y=0, relwidth=1, relheight=1)

def Mostrar_Frame_About():
    Frame_About.place(x=0, y=0, relwidth=1, relheight=1)
######################################################################################################
#Frames y sus canvas
Frame_Principal = tk.Frame(Ventana_Principal, bg="black")
Frame_Principal.pack(fill=tk.BOTH, expand=True)

Canvas_Principal = tk.Canvas(Frame_Principal, bg="black", highlightthickness=0)
Canvas_Principal.pack(fill=tk.BOTH, expand=True)

Frame_Play = tk.Frame(Ventana_Principal, bg="blue", borderwidth=0)
Frame_Play.place(x=0, y=0, relwidth=0, relheight=0)

Canvas_PLay = tk.Canvas(Frame_Play, bg="black", highlightthickness=0)
Canvas_PLay.pack(fill=tk.BOTH, expand=True)

segundo_canvas = tk.Canvas(Frame_Play, bg="blue", highlightthickness=0)
segundo_canvas.pack(fill=tk.BOTH, expand=True)

Frame_About = tk.Frame(Ventana_Principal, bg="green", borderwidth=0)
Frame_About.place(x=0, y=0, relwidth=0, relheight=0)

Canvas_About = tk.Canvas(Frame_About, bg="green", highlightthickness=0)
Canvas_About.pack(fill=tk.BOTH, expand=True)
######################################################################################################
#Fuente de los botones
Font_Button = Font(family="Arial", size="24", weight="bold")
######################################################################################################
#Botones
boton_play = tk.Button(Canvas_Principal, text="Play", font=Font_Button, padx=20, pady=0, command=Mostrar_Frame_Play)
boton_play.pack(pady=(400,20))

boton_about = tk.Button(Canvas_Principal, text="About", font=Font_Button, padx=7, pady=0, command=Mostrar_Frame_About)
boton_about.pack()
######################################################################################################
#Cerrar con escape
def cerrar_con_escape(event):
    if Frame_Play.winfo_ismapped() and event.keysym == "Escape":
        Frame_Play.place_forget()
    elif Frame_About.winfo_ismapped() and event.keysym == "Escape":
        Frame_About.place_forget()
    elif not Frame_Play.winfo_ismapped() and not Frame_About.winfo_ismapped() and event.keysym == "Escape":
        Ventana_Principal.destroy()
Ventana_Principal.bind("<KeyPress>", cerrar_con_escape)
######################################################################################################
#About
######################################################################################################
#Fuentes de About
Font_Main = Font(family="Arial", size="15", weight="bold")
Font_Sub = Font(family="Arial", size="15", weight="bold")
Font_Button_1 = Font(family="Arial", size="19", weight="bold")
######################################################################################################
#Funciones para mostrar los frames
def Mostrar_Frame_Creador1():
    Frame_Creador2.place_forget()
    Frame_Creador1.place(x=0, y=0, relwidth=0.5, relheight=1)

def Mostrar_Frame_Creador2():
    Frame_Creador1.place_forget()
    Frame_Creador2.place(x=0, y=0, relwidth=0.5, relheight=1)
    Frame_Creador.place_forget()

######################################################################################################
#Creadores
Canvas_Creadores = tk.Frame(Canvas_About, bg="white", width=1366, height=256, highlightthickness=0)
Canvas_Creadores.pack(side="top")

Frame_Creador2 = tk.Frame(Canvas_Creadores, bg="white", width=683, height=256, highlightthickness=0)
Frame_Creador2.place(x=0, y=0)

Frame_Creador1 = tk.Frame(Canvas_Creadores, bg="black", width=683, height=256, highlightthickness=0)
Frame_Creador1.place(x=0, y=0)

Label_Creador1 = tk.Label(Frame_Creador1, text="Steven Aguilar Alvarez\n\n3 0557 0029\n\n2028 2024 65", font=Font_Sub, fg="white", bg="black")
Label_Creador1.pack(pady=60)

Label_Creador2 = tk.Label(Frame_Creador2, text="Jannes Ronhaar Flores\n\n3 0557 0029\n\n2028 2024 65", font=Font_Sub, fg="black", bg="white")
Label_Creador2.pack(pady=60)

Frame_Creador = tk.Frame(Canvas_Creadores, bg="white", width=683, height=256, highlightthickness=0)
Frame_Creador.place(x=0, y=0)

#Botones
boton_creador1 = tk.Button(Canvas_Creadores, font=Font_Button_1,text="CREADOR1", command=Mostrar_Frame_Creador2)
boton_creador1.place(relx=0.75, y=50, anchor="n")

boton_creador2 = tk.Button(Canvas_Creadores, font=Font_Button_1, text="CREADOR2", command=Mostrar_Frame_Creador1)
boton_creador2.place(relx=0.75, y=150, anchor="n")
###################
#Información
Canvas_Información = tk.Frame(Canvas_About, bg="black", width=1366, height=256, highlightthickness=0)
Canvas_Información.pack(side="top")

Label_Info = tk.Label(Canvas_Información, text="INFORMATION", font=Font_Main, fg="white", bg="black")
Label_Info.place(relx=0.5, rely=0.1, anchor='center')

Label_Info1 = tk.Label(Canvas_Información, text="FUNDAMENTOS DE SISTEMAS COMPUTACIONALES\nLICENCIATURA EN INGENIERÍA EN COMPUTADORES\n2024\nLUIS ALBERTO CHAVARRÍA\nCOSTA RICA\nVERSION 0.1", font=Font_Main, fg="white", bg="black")
Label_Info1.place(relx=0.5, rely=0.1, anchor='center', y=120)
###################
#Controles
Canvas_Controles = tk.Frame(Canvas_About, bg="white", width=1366, height=256, highlightthickness=0)
Canvas_Controles.pack(side="top")


Label_Controles = tk.Label(Canvas_Controles, text="CONTROLS", font=Font_Main, fg="black", bg="white")
Label_Controles.place(relx=0.5, rely=0.1, anchor='center')
######################################################################################################
#Ventana Play
######################################################################################################

######################################################################################################

Ventana_Principal.mainloop()
pygame.quit()