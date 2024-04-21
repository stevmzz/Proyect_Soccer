from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.font import Font

# Función para cerrar las ventanas
def Cerrar_Ventana(event):
    if 'Ventana_Play' in globals() and Ventana_Play.winfo_exists():
        Ventana_Play.destroy()
    elif 'Ventana_About' in globals() and Ventana_About.winfo_exists():
        Ventana_About.destroy()
    else:
        Ventana_Principal.destroy()

# Función para cambiar la imagen del carrusel de jugadores
def Cambiar_Imagen_Carrusel_Jugadores():
    global imagen_index_jugadores, team_index
    if 'imagen_index_jugadores' not in globals():
        imagen_index_jugadores = 0  # Inicializa imagen_index_jugadores si no está definida
    if imagen_index_jugadores == len(equipos[team_index]) - 1:
        imagen_index_jugadores = 0
    else:
        imagen_index_jugadores += 1

    imagen_actual = equipos[team_index][imagen_index_jugadores]
    canvas_imagen_jugadores.itemconfig(imagen_canvas_jugadores, image=imagen_actual)

# Función para cambiar de equipo para jugador 1
def Cambiar_Equipo_Jugador1():
    global team_index_jugador1
    if team_index_jugador1 == len(equipos) - 1:
        team_index_jugador1 = 0
    else:
        team_index_jugador1 += 1

    nombre_equipo_jugador1.set(nombres_equipos[team_index_jugador1])
    imagen_actual_jugador1 = equipos[team_index_jugador1][imagen_index_jugadores]
    canvas_imagen_jugador1.itemconfig(imagen_canvas_jugador1, image=imagen_actual_jugador1)

# Función para cambiar de jugador para jugador 1
def Cambiar_Jugador_Jugador1():
    global jugador_index_jugador1
    if jugador_index_jugador1 == len(equipos[team_index_jugador1]) - 1:
        jugador_index_jugador1 = 0
    else:
        jugador_index_jugador1 += 1

    imagen_actual_jugador1 = equipos[team_index_jugador1][jugador_index_jugador1]
    canvas_imagen_jugador1.itemconfig(imagen_canvas_jugador1, image=imagen_actual_jugador1)

# Función para cambiar de equipo para jugador 2
def Cambiar_Equipo_Jugador2():
    global team_index_jugador2
    if team_index_jugador2 == len(equipos) - 1:
        team_index_jugador2 = 0
    else:
        team_index_jugador2 += 1

    nombre_equipo_jugador2.set(nombres_equipos[team_index_jugador2])
    imagen_actual_jugador2 = equipos[team_index_jugador2][imagen_index_jugadores]
    canvas_imagen_jugador2.itemconfig(imagen_canvas_jugador2, image=imagen_actual_jugador2)

# Función para cambiar de jugador para jugador 2
def Cambiar_Jugador_Jugador2():
    global jugador_index_jugador2
    if jugador_index_jugador2 == len(equipos[team_index_jugador2]) - 1:
        jugador_index_jugador2 = 0
    else:
        jugador_index_jugador2 += 1

    imagen_actual_jugador2 = equipos[team_index_jugador2][jugador_index_jugador2]
    canvas_imagen_jugador2.itemconfig(imagen_canvas_jugador2, image=imagen_actual_jugador2)

# Función para abrir la ventana de PLAY
def Abrir_Ventana_Play():
    global Ventana_Play, imagen_canvas_jugadores, canvas_imagen_jugadores, canvas_imagen_jugador1, imagen_canvas_jugador1, canvas_imagen_jugador2, imagen_canvas_jugador2, equipos, imagen_index_jugadores, nombres_equipos, team_index_jugador1, team_index_jugador2, jugador_index_jugador1, jugador_index_jugador2
    Ventana_Play = tk.Toplevel()
    Ventana_Play.attributes('-fullscreen', True)
    Ventana_Play.title("PLAY")
    Ventana_Play.config(bg="black")
    Ventana_Play.bind('<Escape>', Cerrar_Ventana)

    # Definir equipos y nombres de equipos
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

    nombres_equipos = ["Manchester City", "París Saint-Germain", "Real Madrid"]

    global imagen_index_jugadores, team_index_jugador1, team_index_jugador2, jugador_index_jugador1, jugador_index_jugador2
    imagen_index_jugadores = 0
    team_index_jugador1 = 0
    team_index_jugador2 = 0
    jugador_index_jugador1 = 0
    jugador_index_jugador2 = 0

    # Configurar label para el nombre del equipo jugador 1
    global nombre_equipo_jugador1
    nombre_equipo_jugador1 = tk.StringVar()
    nombre_equipo_jugador1.set(nombres_equipos[team_index_jugador1])
    label_nombre_equipo_jugador1 = tk.Label(Ventana_Play, textvariable=nombre_equipo_jugador1, font=Font_Label)
    label_nombre_equipo_jugador1.place(x=330,y=100)

    # Configurar carrusel de jugador 1
    imagen_actual_jugador1 = equipos[team_index_jugador1][imagen_index_jugadores]
    global canvas_imagen_jugador1, imagen_canvas_jugador1
    canvas_imagen_jugador1 = tk.Canvas(Ventana_Play, width=300, height=300, bg="white")
    imagen_canvas_jugador1 = canvas_imagen_jugador1.create_image(0, 0, anchor=tk.NW, image=imagen_actual_jugador1)
    canvas_imagen_jugador1.place(x=330, y=200)

    boton_carrusel_jugador1 = tk.Button(Ventana_Play, text="Siguiente Jugador Jugador 1", command=Cambiar_Jugador_Jugador1)
    boton_carrusel_jugador1.place(x=330, y=550)

    # Configurar botón para cambiar de equipo jugador 1
    boton_cambiar_equipo_jugador1 = tk.Button(Ventana_Play, text="Cambiar Equipo Jugador 1", command=Cambiar_Equipo_Jugador1)
    boton_cambiar_equipo_jugador1.place(x=330, y=600)

    # Configurar label para el nombre del equipo jugador 2
    global nombre_equipo_jugador2
    nombre_equipo_jugador2 = tk.StringVar()
    nombre_equipo_jugador2.set(nombres_equipos[team_index_jugador2])
    label_nombre_equipo_jugador2 = tk.Label(Ventana_Play, textvariable=nombre_equipo_jugador2, font=Font_Label)
    label_nombre_equipo_jugador2.place(x=730, y=100)

    # Configurar carrusel de jugador 2
    imagen_actual_jugador2 = equipos[team_index_jugador2][imagen_index_jugadores]
    global canvas_imagen_jugador2, imagen_canvas_jugador2
    canvas_imagen_jugador2 = tk.Canvas(Ventana_Play, width=300, height=300, bg="white")
    imagen_canvas_jugador2 = canvas_imagen_jugador2.create_image(0, 0, anchor=tk.NW, image=imagen_actual_jugador2)
    canvas_imagen_jugador2.place(x=730, y=200)

    boton_carrusel_jugador2 = tk.Button(Ventana_Play, text="Siguiente Jugador Jugador 2", command=Cambiar_Jugador_Jugador2)
    boton_carrusel_jugador2.place(x=730, y=550)

    # Configurar botón para cambiar de equipo jugador 2
    boton_cambiar_equipo_jugador2 = tk.Button(Ventana_Play, text="Cambiar Equipo Jugador 2", command=Cambiar_Equipo_Jugador2)
    boton_cambiar_equipo_jugador2.place(x=730, y=600)
    global boton_listo_jugador1, boton_listo_jugador2
    boton_listo_jugador1 = tk.Button(Ventana_Play, text="listo", command=Abrir_Ventana_Juego)
    boton_listo_jugador1.place(x=330, y=650)

    boton_listo_jugador2 = tk.Button(Ventana_Play, text="listo", command=Abrir_Ventana_Juego)
    boton_listo_jugador2.place(x=730, y=650)

def Abrir_Ventana_Juego():
    if boton_listo_jugador1["text"] == "LISTO" and boton_listo_jugador2["text"] == "LISTO":
        Ventana_Juego = tk.Toplevel(Ventana_Play)
        Ventana_Juego.attributes('-fullscreen', True)
        Ventana_Juego.title("JUEGO")
        Ventana_Juego.config(bg="black")
        Ventana_Juego.bind('<Escape>', Cerrar_Ventana)
    else:
        boton_listo_jugador1.config(text="LISTO")
        boton_listo_jugador2.config(text="LISTO")





# Función para abrir la ventana ABOUT
def Abrir_Ventana_About():
    global Ventana_About, Font_Label
    Ventana_About = tk.Toplevel()
    Ventana_About.attributes('-fullscreen', True)
    Ventana_About.title("ABOUT")
    Ventana_About.config(bg="black")
    Ventana_About.bind('<Escape>', Cerrar_Ventana)

    Canvas_Creadores = tk.Canvas(Ventana_About, width=1366, height=384)
    Canvas_Creadores.pack()

    Canvas_Info = tk.Canvas(Ventana_About)
    Canvas_Info.pack()

# Ventana Principal
Ventana_Principal = tk.Tk()
Ventana_Principal.attributes('-fullscreen', True)
Ventana_Principal.title("MAIN")
Ventana_Principal.bind('<Escape>', Cerrar_Ventana)
Ventana_Principal.config(background="black")

# Fuentes
Font_Button = Font(family="Courier New", size=24, weight="bold")
Font_Label = Font(family="Courier New", size=24, weight="bold")

# Botones
Boton_Play = tk.Button(Ventana_Principal, text="PLAY", font=Font_Button, command=Abrir_Ventana_Play)
Boton_Play.pack(pady=(500, 0))

Boton_About = tk.Button(Ventana_Principal, text="ABOUT", font=Font_Button, command=Abrir_Ventana_About)
Boton_About.pack(pady=10)

Label_Version = Label(Ventana_Principal, text="version: 0.1", font=("Courier New", 10, "bold"), fg="white", bg="black")
Label_Version.place(x=0, y=0)

Ventana_Principal.mainloop()
