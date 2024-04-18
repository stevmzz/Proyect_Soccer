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
#
#
######################################################################################################
#Ventana Principal
######################################################################################################
Ventana_Principal = tk.Tk()
Ventana_Principal.attributes('-fullscreen', True)
Ventana_Principal.title("fundamentos")
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
    Frame_Creador1.place(x=0, y=0, relwidth=1, relheight=1)

def Mostrar_Frame_Creador2():
    Frame_Creador1.place_forget()
    Frame_Creador2.place(x=0, y=0, relwidth=1, relheight=1)
######################################################################################################
#Creadores

Canvas_Creadores = tk.Canvas(Canvas_About, bg="white", highlightthickness=0, width=1366, height=256)
Canvas_Creadores.place()

Frame_Creador1 = tk.Frame(Canvas_Creadores, bg="black", width=683, height=256, highlightthickness=0)
Frame_Creador1.place(x=0, y=0)

Frame_Creador2 = tk.Frame(Canvas_Creadores, bg="white", width=683, height=256, highlightthickness=0)
Frame_Creador2.place(x=0, y=0)

#Botones
boton_creador1 = tk.Button(Canvas_Creadores, font=Font_Button_1,text="CREADOR1", command=Mostrar_Frame_Creador1)
boton_creador1.pack()

boton_creador2 = tk.Button(Canvas_Creadores, font=Font_Button_1, text="CREADOR2", command=Mostrar_Frame_Creador2)
boton_creador2.pack()


######################################################################################################

Ventana_Principal.mainloop()


Frame_Creador2 = tk.Frame(Canvas_Creadores, bg="white", width=683, height=256, highlightthickness=0)
Frame_Creador2.place(x=0, y=0)

Frame_Creador1 = tk.Frame(Canvas_Creadores, bg="green", width=683, height=256, highlightthickness=0)
Frame_Creador1.place(x=0, y=0)

Frame_Creador = tk.Frame(Canvas_Creadores, bg="green", width=683, height=256, highlightthickness=0)
Frame_Creador.place(x=0, y=0, anchor='w')

Label_Creador1 = tk.Label(Frame_Creador1, text="Steven")
Label_Creador1.pack()