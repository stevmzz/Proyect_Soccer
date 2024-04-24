import tkinter as tk
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import PhotoImage
import pygame
from pygame.locals import *
import random
import time
import os
##########################################################################################################
size = 44
cantidad_bombas = 20
probabilidad_llave = 50
points = 0
cantidad_enemigos = 2
velocidad_enemigos_1 = 500
velocidad_enemigos_2 = 500
##########################################################################################################
def check_mute_state():
    pygame.mixer.init()
    if os.path.exists("mute_state.txt"):
        with open("mute_state.txt", "r+") as file:
            mute_state = file.read().strip()
            file.seek(0)  # Mover el cursor al principio del archivo
            file.truncate()  # Borrar el contenido del archivo
        if mute_state == "1":
            pygame.mixer.music.set_volume(0)  # Silenciar la música
            pygame.mixer.pause()  # Pausar todos los efectos de sonido
        else:
            pygame.mixer.music.set_volume(1)  # Restaurar volumen de la música
            pygame.mixer.unpause()  # Reanudar efectos de sonido pausados
    else:
        pygame.mixer.music.set_volume(1)  # Activar volumen de la música
        pygame.mixer.unpause()  # Activar efectos de sonido por defecto

check_mute_state()
##########################################################################################################
#Música
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('sounds/𝗱𝗼𝗿𝗶𝗮𝗻 𝗰𝗼𝗻𝗰𝗲𝗽𝘁 - 𝗵𝗶𝗱𝗲 (𝗰𝘀𝟬𝟭) (𝗺𝘆𝘀𝘁𝗲𝗿𝗶𝗼𝘂𝘀 𝗱𝘂𝗻𝗴𝗲𝗼𝗻_𝘀𝗹𝗼𝘄𝗲𝗱 + 𝗿𝗲𝘃𝗲𝗿𝗯).mp3')
pygame.mixer.music.play(-1)
##########################################################################################################
# Maze
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
##########################################################################################################
# Ventana Principal
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

ventana_juego = tk.Tk()
ventana_juego.title("Bomberman Maze")
ventana_juego.attributes('-fullscreen', True)  # Hacer la ventana fullscreen
ventana_juego.configure(bg='black')  # Establecer el color de fondo a negro

content_width = 1033
content_height = 760

def close_window(event):
    ventana_juego.destroy()

center_window(ventana_juego, content_width, content_height)
##########################################################################################################
#Canvas
canvas_superior = tk.Canvas(ventana_juego, width=1033, height=100, background="white")
canvas_superior.pack()

canvas_lifebar = tk.Canvas(canvas_superior, width=200, height=100, background="white")
canvas_lifebar.pack(side="left")

canvas_points = tk.Canvas(canvas_superior, width=400, height=100, background="white")
canvas_points.pack(side="left")

Font_Main = Font(family="Courier New", size=20, weight="bold")

# Etiqueta para mostrar el tiempo
time_label = tk.Label(canvas_points, text="TIME:0:00", font=Font_Main, fg="white", bg="black", padx=20)
time_label.pack(side="left")

points_label = tk.Label(canvas_points, text=f"POINTS: 00000", font=Font_Main, fg="black", bg="white", padx=20)
points_label.pack(side="left")

bombs_label = tk.Label(canvas_points, text=f"BOMBS: {cantidad_bombas}", font=Font_Main, fg="white", bg="black", padx=20)
bombs_label.pack(side="left")

key_label = tk.Label(canvas_points, text="KEY: NOT", font=Font_Main, fg="black", bg="white", padx=20)
key_label.pack(side="left")

# Función para actualizar el tiempo
def update_time():
    global start_time
    current_time = int(time.time() - start_time)
    minutes = current_time // 60
    seconds = current_time % 60
    
    time_label.config(text=f"TIME:{minutes}:{seconds:02d}")
    ventana_juego.after(1000, update_time)  # Llama a esta función cada segundo

# Inicia el cronómetro al comenzar el juego
start_time = time.time()
update_time()

canvas_maze = tk.Canvas(ventana_juego, width=1000, height=683)
canvas_maze.pack()
##########################################################################################################
# Imágenes de vida
life_image1 = Image.open("images/vida.png")
life_image1 = life_image1.resize((30,30), Image.LANCZOS)
life_image1_tk = ImageTk.PhotoImage(life_image1)
life_id1 = canvas_lifebar.create_image(28, 38, anchor="nw", image=life_image1_tk)

life_image2 = Image.open("images/vida.png")
life_image2 = life_image2.resize((30,30), Image.LANCZOS)
life_image2_tk = ImageTk.PhotoImage(life_image2)
life_id2 = canvas_lifebar.create_image(88, 38, anchor="nw", image=life_image2_tk)

life_image3 = Image.open("images/vida.png")
life_image3 = life_image3.resize((30,30), Image.LANCZOS)
life_image3_tk = ImageTk.PhotoImage(life_image3)
life_id3 = canvas_lifebar.create_image(148, 38, anchor="nw", image=life_image3_tk)
##########################################################################################################
#Texturas
muro = Image.open("images/textures/piedradura3.jpg")
muro = muro.resize((size, size), Image.LANCZOS)  
muro = ImageTk.PhotoImage(muro)

cesped = Image.open("images/textures/cesped2.png")
cesped = cesped.resize((size, size), Image.LANCZOS) 
cesped = ImageTk.PhotoImage(cesped)

puerta_cesped = Image.open("images/textures/puertacesped.png")
puerta_cesped = puerta_cesped.resize((size, size), Image.LANCZOS) 
puerta_cesped = ImageTk.PhotoImage(puerta_cesped)

destructible = Image.open("images/textures/destructible3.png")
destructible = destructible.resize((size, size), Image.LANCZOS)
destructible_tk = ImageTk.PhotoImage(destructible)
##########################################################################################################
bloques_nivel_1 = [(1, 2), (2, 7), (4, 7), (6, 9), (8, 7), (6, 9), (8, 3), (4, 1), (5, 1), (12, 7), (14, 7), (4, 13), (8, 1), (10, 5), (12, 7), (11, 7), (8, 3), (7, 3), (14, 7), (16, 3), (8, 13), (10, 13), (10, 11), (14, 13), (15, 13), (13, 8), (12, 13), (15, 7), (15, 12), (16, 7), (15, 10), (14, 9), (13, 12), (14, 13), (10, 1), (10, 3), (13, 4), (16, 3), (15, 4), (16, 9), (17, 7), (21, 13), (21, 12), (20, 13), (17, 7), (16, 13), (11, 13), (11, 12), (1, 13), (1, 12), (1, 11), (2, 13), (3, 10), (1, 3), (3, 2), (3, 3), (1, 5), (21, 1), (20, 1), (15, 1), (3, 7), (21, 7), (21, 6), (21, 5), (21, 10), (21, 9), (20, 9), (19, 9), (17, 9), (17, 10), (18,11), (7, 6), (5, 6), (6, 7), (6, 5)]
bloques_nivel_2 = [(1, 2), (2, 7), (4, 7), (6, 9), (8, 7), (6, 9), (8, 3), (4, 1), (5, 1), (12, 7), (14, 7), (4, 13), (8, 1), (10, 5), (12, 7), (11, 7), (8, 3), (7, 3), (14, 7), (16, 3), (8, 13), (10, 13), (10, 11), (14, 13), (15, 13), (13, 8), (12, 13), (15, 7), (15, 12), (16, 7), (15, 10), (14, 9), (13, 12), (14, 13), (10, 1), (10, 3), (13, 4), (16, 3), (15, 4), (16, 9), (17, 7), (21, 13), (21, 12), (20, 13), (17, 7), (16, 13), (11, 13), (11, 12), (1, 13), (1, 12), (1, 11), (2, 13), (3, 10), (1, 3), (3, 2), (3, 3), (1, 5), (21, 1), (20, 1), (15, 1), (3, 7), (21, 7), (21, 6), (21, 5), (21, 10), (21, 9), (20, 9), (19, 9), (17, 9), (17, 10), (18,11), (7, 6), (5, 6), (6, 7), (6, 5), (6, 11), (6, 13), (7, 12), (5, 12)]
bloques_nivel_3 = [(1, 2), (2, 7), (4, 7), (6, 9), (8, 7), (6, 9), (8, 3), (4, 1), (5, 1), (12, 7), (14, 7), (4, 13), (8, 1), (10, 5), (12, 7), (11, 7), (8, 3), (7, 3), (14, 7), (16, 3), (8, 13), (10, 13), (10, 11), (14, 13), (15, 13), (13, 8), (12, 13), (15, 7), (15, 12), (16, 7), (15, 10), (14, 9), (13, 12), (14, 13), (10, 1), (10, 3), (13, 4), (16, 3), (15, 4), (16, 9), (17, 7), (21, 13), (21, 12), (20, 13), (17, 7), (16, 13), (11, 13), (11, 12), (1, 13), (1, 12), (1, 11), (2, 13), (3, 10), (1, 3), (3, 2), (3, 3), (1, 5), (21, 1), (20, 1), (15, 1), (3, 7), (21, 7), (21, 6), (21, 5), (21, 10), (21, 9), (20, 9), (19, 9), (17, 9), (17, 10), (18,11), (7, 6), (5, 6), (6, 7), (6, 5), (6, 11), (6, 13), (7, 12), (5, 12), (8, 9), (8, 11), (7, 10), (9, 10), (18, 5), (18, 3), (17, 4), (19, 4)]


def draw_maze_recursive(y=0, x=0):
    if y >= len(maze):  # Caso base: si llegamos al final del laberinto, terminamos la recursión
        return
    
    if maze[y][x] == 1:
        canvas_maze.create_image(x * size, y * size, anchor=tk.NW, image=muro)
    elif maze[y][x] == 2:
        canvas_maze.create_image(x * size, y * size, anchor=tk.NW, image=puerta_cesped)
    else:
        canvas_maze.create_image(x * size, y * size, anchor=tk.NW, image=cesped)
        
    next_x = x + 1
    next_y = y
    if next_x >= len(maze[y]):
        next_x = 0
        next_y = y + 1
    
    draw_maze_recursive(next_y, next_x)
draw_maze_recursive()

def encontrar_posicion_inicial():
  return size, size
posicion_inicial = encontrar_posicion_inicial()
##########################################################################################################
# Movimiento del Personaje
def iniciar_juego():
    global player_x, player_y, player_image_tk, player_image, player_id, skin_seleccionada

    # Leer la skin seleccionada desde el archivo de texto
    with open("skin_seleccionada.txt", "r") as file:
        skin_seleccionada = file.readline()

    player_x = posicion_inicial[0]
    player_y = posicion_inicial[1]

    # Imprime la ruta de la imagen antes de cargarla
    ruta_imagen = f"images/skin1 - copia/{skin_seleccionada} frente.png"
    print("Ruta de la imagen:", ruta_imagen)

    # Crear la imagen del jugador según la skin seleccionada
    player_image = Image.open(ruta_imagen)
    player_image = player_image.resize((size, size), Image.LANCZOS)
    player_image_tk = ImageTk.PhotoImage(player_image)
    player_id = canvas_maze.create_image(player_x, player_y, anchor="nw", image=player_image_tk)
iniciar_juego()

def move_up(event):
    global player_x, player_y, player_image_tk, player_image, skin_seleccionada
    new_y = player_y - size  # Tamaño de la casilla
    if new_y >= 0 and maze[new_y // size][player_x // size] == 0 and not verificar_colision_bloques_destructibles_recursivo(player_x, new_y):
        player_y = new_y
        canvas_maze.coords(player_id, player_x, player_y)
        if verificar_colision_con_enemigos_recursivo(player_x, player_y):
            return
        player_image = Image.open(f"images/skin1 - copia/{skin_seleccionada} atras.png")
        player_image = player_image.resize((size, size), Image.LANCZOS)
        player_image_tk = ImageTk.PhotoImage(player_image)
        canvas_maze.itemconfig(player_id, image=player_image_tk)

def move_down(event):
    global player_x, player_y, player_image_tk, player_image, skin_seleccionada
    new_y = player_y + size  # Tamaño de la casilla
    if new_y < len(maze) * size and maze[new_y // size][player_x // size] == 0 and not verificar_colision_bloques_destructibles_recursivo(player_x, new_y):
        player_y = new_y
        canvas_maze.coords(player_id, player_x, player_y)
        if verificar_colision_con_enemigos_recursivo(player_x, player_y):
            return
        player_image = Image.open(f"images/skin1 - copia/{skin_seleccionada} frente.png")
        player_image = player_image.resize((size, size), Image.LANCZOS)
        player_image_tk = ImageTk.PhotoImage(player_image)
        canvas_maze.itemconfig(player_id, image=player_image_tk)

def move_left(event):
    global player_x, player_y, player_image_tk, player_image, skin_seleccionada
    new_x = player_x - size  # Tamaño de la casilla
    if new_x >= 0 and maze[player_y // size][new_x // size] == 0 and not verificar_colision_bloques_destructibles_recursivo(new_x, player_y):
        player_x = new_x
        canvas_maze.coords(player_id, player_x, player_y)
        if verificar_colision_con_enemigos_recursivo(player_x, player_y):
            return
        player_image = Image.open(f"images/skin1 - copia/{skin_seleccionada} izq.png")
        player_image = player_image.resize((size, size), Image.LANCZOS)
        player_image_tk = ImageTk.PhotoImage(player_image)
        canvas_maze.itemconfig(player_id, image=player_image_tk)

def move_right(event):
    global player_x, player_y, player_image_tk, player_image, skin_seleccionada
    new_x = player_x + size  # Tamaño de la casilla
    if new_x < len(maze[0]) * size and maze[player_y // size][new_x // size] == 0 and not verificar_colision_bloques_destructibles_recursivo(new_x, player_y):
        player_x = new_x
        canvas_maze.coords(player_id, player_x, player_y)
        if verificar_colision_con_enemigos_recursivo(player_x, player_y):
            return
        player_image = Image.open(f"images/skin1 - copia/{skin_seleccionada} der.png")
        player_image = player_image.resize((size, size), Image.LANCZOS)
        player_image_tk = ImageTk.PhotoImage(player_image)
        canvas_maze.itemconfig(player_id, image=player_image_tk)

def verificar_colision_bloques_destructibles_recursivo(new_x, new_y, index=0):
    if index >= len(bloques_nivel_1):
        return False  # Caso base: no hay colisión
    
    x, y = bloques_nivel_1[index]
    if new_x == x * size and new_y == y * size:
        return True  # Hay colisión con un bloque destructible
    
    return verificar_colision_bloques_destructibles_recursivo(new_x, new_y, index + 1)
##########################################################################################################
#Quitar Vida
vidas_restantes = 3

def quitar_vida():
    global life_id1, life_id2, life_id3, vidas_restantes

    if vidas_restantes == 3:
        canvas_lifebar.delete(life_id3)
        life_id3 = None
    elif vidas_restantes == 2:
        canvas_lifebar.delete(life_id2)
        life_id2 = None
    elif vidas_restantes == 1:
        canvas_lifebar.delete(life_id1)
        life_id1 = None
        open_game_over_loss()

    vidas_restantes -= 1
##########################################################################################################
def open_game_over_loss():
    game_over_window = tk.Toplevel()
    
    game_over_window.attributes('-fullscreen', True)
    
    label_game_over = tk.Label(game_over_window, text="GAME OVER LOSS", font=("Arial", 24, "bold"))
    label_game_over.pack(expand=True)  # Expandir el Label para llenar la ventana
    
def open_game_over_win():
    game_over_win_window = tk.Toplevel()
    
    game_over_win_window.attributes('-fullscreen', True)
    
    label_game_over = tk.Label(game_over_win_window, text="GAME OVER WIN", font=("Arial", 24, "bold"))
    label_game_over.pack(expand=True)  # Expandir el Label para llenar la ventana
##########################################################################################################
#Enemigos
enemigos_ids = []

enemigo_image = Image.open("images/enemigo1.png")
enemigo_image = enemigo_image.resize((size, size), Image.LANCZOS)
enemigo_image_tk = ImageTk.PhotoImage(enemigo_image)

enemigo_image2 = Image.open("images/enemigo2.png")
enemigo_image2 = enemigo_image2.resize((size, size), Image.LANCZOS)
enemigo_image2_tk = ImageTk.PhotoImage(enemigo_image2)

def generar_enemigos(cantidad_enemigos, enemigo_ids, enemigo_image_tk):
    if cantidad_enemigos == 0:
        return
    
    # Buscar una posición aleatoria vacía en el laberinto
    while True:
        enemigo_x = random.randint(0, len(maze[0]) - 1)
        enemigo_y = random.randint(0, len(maze) - 1)
        if maze[enemigo_y][enemigo_x] == 0:
            break
    
    # Crear la imagen del enemigo en el canvas
    enemigo_id = canvas_maze.create_image(enemigo_x * size, enemigo_y * size, anchor='nw', image=enemigo_image_tk)
    enemigo_ids.append(enemigo_id)
    
    # Generar el siguiente enemigo recursivamente
    generar_enemigos(cantidad_enemigos - 1, enemigo_ids, enemigo_image_tk)

# Llamar a la función para generar los enemigos tipo 1
enemigo1_ids = []
generar_enemigos(cantidad_enemigos, enemigo1_ids, enemigo_image_tk)

# Llamar a la función para generar los enemigos tipo 2
enemigo2_ids = []
generar_enemigos(cantidad_enemigos, enemigo2_ids, enemigo_image2_tk)

import random

def mover_enemigo_1_recursivo(enemigo_id, velocidad):
    direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])
    mover_enemigo_recursivo(enemigo_id, velocidad, direccion)

def mover_enemigo_2_recursivo(enemigo_id, velocidad):
    direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])
    mover_enemigo_recursivo(enemigo_id, velocidad, direccion)

def mover_enemigo_recursivo(enemigo_id, velocidad, direccion):
    x, y = canvas_maze.coords(enemigo_id)
    nueva_x, nueva_y = calcular_nueva_posicion(x, y, direccion)

    if es_movimiento_valido(nueva_x, nueva_y) and not verificar_colision_bloques_destructibles_recursivo(nueva_x, nueva_y):
        canvas_maze.coords(enemigo_id, nueva_x, nueva_y)

    ventana_juego.after(velocidad, mover_enemigo_recursivo, enemigo_id, velocidad, direccion)

def calcular_nueva_posicion(x, y, direccion):
    if direccion == "arriba":
        return x, y - size
    elif direccion == "abajo":
        return x, y + size
    elif direccion == "izquierda":
        return x - size, y
    elif direccion == "derecha":
        return x + size, y
    else:
        return x, y

def es_movimiento_valido(x, y):
    return 0 <= x < len(maze[0]) * size and 0 <= y < len(maze) * size and maze[int(y // size)][int(x // size)] == 0

def iniciar_movimiento_enemigos_1(index=0):
    if index < len(enemigo1_ids):
        enemigo_id = enemigo1_ids[index]
        mover_enemigo_1_recursivo(enemigo_id, velocidad_enemigos_1)
        ventana_juego.after(velocidad_enemigos_1, iniciar_movimiento_enemigos_1, index + 1)

# Función para llamar recursivamente al movimiento de enemigos tipo 2
def iniciar_movimiento_enemigos_2(index=0):
    if index < len(enemigo2_ids):
        enemigo_id = enemigo2_ids[index]
        mover_enemigo_2_recursivo(enemigo_id, velocidad_enemigos_2)
        ventana_juego.after(velocidad_enemigos_2, iniciar_movimiento_enemigos_2, index + 1)

# Llamar inicialmente a las funciones recursivas
iniciar_movimiento_enemigos_1()
iniciar_movimiento_enemigos_2()

def verificar_colision_con_enemigos_recursivo(player_x, player_y, index=0):
    global enemigo1_ids, enemigo2_ids
    
    # Combina los IDs de los enemigos tipo 1 y tipo 2
    enemigos_ids = enemigo1_ids + enemigo2_ids

    if index >= len(enemigos_ids):
        return False  # No hay más enemigos que verificar, no hay colisión
    
    enemigo_id = enemigos_ids[index]
    enemigo_x, enemigo_y = canvas_maze.coords(enemigo_id)
    
    # Verificar si el jugador y el enemigo se superponen (dentro de una tolerancia)
    if abs(player_x - enemigo_x) < size and abs(player_y - enemigo_y) < size:
        quitar_vida()
        return True
    
    return verificar_colision_con_enemigos_recursivo(player_x, player_y, index + 1)
##########################################################################################################
#Bomba
explosion_tamaño = 75

# Cargar la imagen de la bomba y los frames de la explosión
bomba_image = PhotoImage(file="images/bomba.png")
bomba_image = bomba_image.subsample(int(bomba_image.width() / size), int(bomba_image.height() / size))  # Redimensionar la imagen
frames_explosion = list(map(lambda i: PhotoImage(file=f"images/explotion frames/frame{i}.png"), range(7)))
frames_explosion_resized = list(map(lambda frame: frame.subsample(int(frame.width() / explosion_tamaño), int(frame.height() / explosion_tamaño)), frames_explosion))
bomba_colocada = False
bomba_x = -1
bomba_y = -1
tiempo_explosion = 3
velocidad_explosion = 100

def mostrar_frames_explosion(frames, index, x, y, bomba_x, bomba_y):
    global bloques_destructibles_destruidos, enemigos_ids, explosion_x, explosion_y
    if index < len(frames):
        canvas_maze.create_image(x, y, anchor="nw", image=frames[index], tags=("explosion", "elemento"))
        ventana_juego.update()
        ventana_juego.after(velocidad_explosion, lambda: canvas_maze.delete("explosion"))
        
        # Almacenar la posición de la explosión
        explosion_x = bomba_x
        explosion_y = bomba_y
        
        # Verificar si el jugador está dentro del rango de la explosión solo en el primer frame
        if index == 0:
            if abs(player_x - explosion_x) <= explosion_tamaño and abs(player_y - explosion_y) <= explosion_tamaño:
                quitar_vida()
        
        # Llamar a la nueva función para manejar la destrucción de los bloques destructibles
        destruir_bloques_destructibles(bomba_x // size, bomba_y // size, explosion_tamaño)
        
        # Verificar si algún enemigo está dentro del rango de la explosión
        eliminar_enemigos_recursivo(bomba_x, bomba_y)
        
        ventana_juego.after(100, lambda: mostrar_frames_explosion(frames, index + 1, x-10, y-10, bomba_x, bomba_y))

def eliminar_enemigos_recursivo(bomba_x, bomba_y, index=0):
    global enemigo1_ids, enemigo2_ids

    if index < len(enemigo1_ids):
        enemigo_id = enemigo1_ids[index]
        enemigo_x, enemigo_y = canvas_maze.coords(enemigo_id)

        if abs(enemigo_x - bomba_x) <= explosion_tamaño and abs(enemigo_y - bomba_y) <= explosion_tamaño:
            # Eliminar al enemigo del juego
            canvas_maze.delete(enemigo_id)
            aumentar_puntos(500)
            enemigo1_ids.pop(index)
            eliminar_enemigos_recursivo(bomba_x, bomba_y, index)  # Llamada recursiva con el mismo índice para procesar el siguiente enemigo
        else:
            eliminar_enemigos_recursivo(bomba_x, bomba_y, index + 1)  # Llamada recursiva con el siguiente índice
    elif index < len(enemigo1_ids) + len(enemigo2_ids):  # Verificar para enemigo2_ids
        enemigo_id = enemigo2_ids[index - len(enemigo1_ids)]  # Ajuste del índice para el segundo tipo de enemigo
        enemigo_x, enemigo_y = canvas_maze.coords(enemigo_id)

        if abs(enemigo_x - bomba_x) <= explosion_tamaño and abs(enemigo_y - bomba_y) <= explosion_tamaño:
            # Eliminar al enemigo del juego
            canvas_maze.delete(enemigo_id)
            aumentar_puntos(500)
            enemigo2_ids.pop(index - len(enemigo1_ids))  # Ajuste del índice para el segundo tipo de enemigo
            eliminar_enemigos_recursivo(bomba_x, bomba_y, index)  # Llamada recursiva con el mismo índice para procesar el siguiente enemigo
        else:
            eliminar_enemigos_recursivo(bomba_x, bomba_y, index + 1)  # Llamada recursiva con el siguiente índice

def colocar_bomba(event):
    global bomba_colocada, bomba_x, bomba_y, cantidad_bombas
    if not bomba_colocada:
        bomba_x = player_x // size
        bomba_y = player_y // size
        canvas_maze.create_image(bomba_x * size, bomba_y * size, anchor="nw", image=bomba_image, tags=("bomba", "elemento"))
        bomba_colocada = True
        ventana_juego.after(tiempo_explosion * 1000, explotar_bomba_recursivo)
        bomba_colocada = True
        cantidad_bombas -= 1  # Disminuir la cantidad de bombas disponibles
        bombs_label.config(text=f"BOMBS: {cantidad_bombas}")
        if cantidad_bombas<=9:
            bombs_label.config(text=f"BOMBS: 0{cantidad_bombas}")
        if cantidad_bombas == 0:  # Verificar si la cantidad de bombas es cero
            open_game_over_loss()

# Función explotar_bomba
def explotar_bomba_recursivo():
    global bomba_colocada, bomba_x, bomba_y
    canvas_maze.delete("bomba")
    bomba_colocada = False
    x = bomba_x * size
    y = bomba_y * size
    mostrar_frames_explosion(frames_explosion_resized, 0, x, y, x, y)
##########################################################################################################
bloques_destructibles_destruidos = []

def destruir_bloques_destructibles(bomba_x, bomba_y, explosion_tamaño):
    global bloques_destructibles, bloques_destructibles_destruidos, maze, points

    def destruir_bloque_recursivo(index=0):
        if index >= len(bloques_destructibles):
            return
        
        x, y = bloques_destructibles[index]
        
        if abs(x - bomba_x) <= explosion_tamaño // size and abs(y - bomba_y) <= explosion_tamaño // size:
            
            canvas_maze.delete(f"bloque_destructible_{x}_{y}")
            maze[y][x] = 0
            canvas_maze.itemconfig(f"bloque_destructible_{x}_{y}", state="hidden")
            bloques_destructibles_destruidos.append((x, y))
            bloques_destructibles.pop(index)
            
            # Aumentar los puntos en 100
            aumentar_puntos(100)
            
            destruir_bloque_recursivo(index)
        else:
            destruir_bloque_recursivo(index + 1)

    destruir_bloque_recursivo()

def aumentar_puntos(puntos_a_sumar):
    global points, points_label
    points += puntos_a_sumar
    points_label.config(text=f"POINTS: 00{points}")
    if points >= 1000:
        points_label.config(text=f"POINTS: 0{points}")
        if points >= 10000:
            points_label.config(text=f"POINTS: {points}")
    guardar_puntos_totales(points)
##########################################################################################################
# Generación de Llave
key_x = -1
key_y = -1
key_obtained = False

def generar_llave_aleatoria(maze, key_image, bloques_destructibles):
    global key_x, key_y, key_obtained, key_id

    def buscar_bloque_destructible_recursivo(index=0):
        if index >= len(bloques_destructibles):
            return None  # Caso base: no se encontró un bloque destructible libre

        x, y = bloques_destructibles[index]
        if random.randint(1, 100) <= probabilidad_llave:  
            return (x, y)  # Devolver las coordenadas del bloque destructible

        return buscar_bloque_destructible_recursivo(index + 1)

    celda_libre = buscar_bloque_destructible_recursivo()
    if celda_libre:
        key_x, key_y = celda_libre
        key_id = canvas_maze.create_image(key_x * size, key_y * size, anchor=tk.NW, image=key_image, tags=("llave"))
        canvas_maze.tag_lower(key_id, f"bloque_destructible_{key_x}_{key_y}")
    else:
        key_x = key_y = -1  # Restablecer las coordenadas de la llave si no se encuentra una posición válida

def obtener_llave(event):
    global key_x, key_y, player_x, player_y, key_label, key_obtained, key_id

    if key_x != -1 and key_y != -1 and player_x == key_x * size and player_y == key_y * size:
        key_label.config(text="KEY: YES")
        canvas_maze.delete(key_id)  # Ocultar la imagen de la llave
        key_obtained = True
        aumentar_puntos(500)

key_image = Image.open("images/objs/keyicon.png")
key_image = key_image.resize((size, size), Image.LANCZOS)
key_image_tk = ImageTk.PhotoImage(key_image)

generar_llave_aleatoria(maze, key_image_tk, bloques_destructibles)
##########################################################################################################
# Puerta
door_location = (12, 13)
door_image = Image.open("images/objs/door_closed.png")
door_image = door_image.resize((size, size), Image.LANCZOS)
door_image_tk = ImageTk.PhotoImage(door_image)
door_id = canvas_maze.create_image(door_location[0] * size, door_location[1] * size, anchor=tk.NW, image=door_image_tk, tags=("puerta"))
canvas_maze.itemconfig(door_id, state="hidden")

def abrir_puerta(event):
    global key_obtained, door_location, door_id, nivel_actual

    if key_obtained and player_x // size == door_location[0] and player_y // size == door_location[1]:
        canvas_maze.delete(door_id)
        if nivel_actual == 1:
            nivel_actual = 2
            reiniciar_juego(nivel_actual)
        elif nivel_actual == 2:
            nivel_actual = 3
            reiniciar_juego(nivel_actual)
        elif nivel_actual == 3:
            open_game_over_win()
##########################################################################################################
#Controles
ventana_juego.bind("k", abrir_puerta)
ventana_juego.bind("j", obtener_llave)
ventana_juego.bind("K", abrir_puerta)
ventana_juego.bind("J", obtener_llave)
ventana_juego.bind('<Escape>', close_window)
ventana_juego.bind("<space>", colocar_bomba)

ventana_juego.bind("<Up>", move_up)
ventana_juego.bind("<Down>", move_down)
ventana_juego.bind("<Left>", move_left)
ventana_juego.bind("<Right>", move_right)
ventana_juego.bind("w", move_up)
ventana_juego.bind("s", move_down)
ventana_juego.bind("a", move_left)
ventana_juego.bind("d", move_right)
ventana_juego.bind("W", move_up)
ventana_juego.bind("S", move_down)
ventana_juego.bind("A", move_left)
ventana_juego.bind("D", move_right)
##########################################################################################################
#Ranking
def guardar_puntos_totales(puntos_finales):
    with open('puntos.txt', 'w') as file:
        file.write(str(puntos_finales))
##########################################################################################################
def reiniciar_juego(nivel):
    global player_x, player_y, cantidad_enemigos, probabilidad_llave, door_location, player_id, bloques_destructibles, maze

    if nivel_actual == 2:
        player_x, player_y = encontrar_posicion_inicial()
        generar_llave_aleatoria(maze, key_image_tk, bloques_destructibles)
        player_id = canvas_maze.create_image(player_x, player_y, anchor="nw", image=player_image_tk)
        key_label.config(text="KEY: NOT")

        # Limpiar los bloques destructibles existentes
        canvas_maze.delete("bloque_destructible")

        # Definir los bloques destructibles para el nivel 2
        definir_bloques_destructibles_recursivo(nivel=2)
        
        cantidad_bombas = 15
        bombs_label.config(text=f"BOMBS: {cantidad_bombas}")

    elif nivel_actual == 3:
        player_x, player_y = encontrar_posicion_inicial()
        generar_llave_aleatoria(maze, key_image_tk, bloques_destructibles)
        player_id = canvas_maze.create_image(player_x, player_y, anchor="nw", image=player_image_tk)
        key_label.config(text="KEY: NOT")

        # Limpiar los bloques destructibles existentes
        canvas_maze.delete("bloque_destructible")

        # Definir los bloques destructibles para el nivel 3
        definir_bloques_destructibles_recursivo(nivel=3)

        cantidad_bombas = 10
        bombs_label.config(text=f"BOMBS: {cantidad_bombas}")

def definir_bloques_destructibles_recursivo(nivel, index=0):
    global bloques_destructibles

    if nivel == 1:
        bloques_destructibles = bloques_nivel_1.copy()
    elif nivel == 2:
        bloques_destructibles = bloques_nivel_2.copy()
    elif nivel == 3:
        bloques_destructibles = bloques_nivel_3.copy()

    if index < len(bloques_destructibles):
        x, y = bloques_destructibles[index]
        canvas_maze.create_image(x * size, y * size, anchor=tk.NW, image=destructible_tk, tags=f"bloque_destructible_{x}_{y}")
        definir_bloques_destructibles_recursivo(nivel, index + 1)

nivel_actual = 1
reiniciar_juego(nivel_actual)
##########################################################################################################

ventana_juego.mainloop()
 