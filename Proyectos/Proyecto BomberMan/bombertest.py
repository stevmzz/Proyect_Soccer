import tkinter as tk # Tkinter
from PIL import Image, ImageTk # Imágenes
from tkinter.font import Font # Fuentes
from tkinter import PhotoImage # Imágenes
import pygame # Música
import random # Aleatorio
import time # Tiempo
import os # Manejar rutas y archivos
##########################################################################################################
tamaño = 44  # Tamaño del juego
cantidad_bombas = 35  # Cantidad de bombas
probabilidad_llave = 50  # Probabilidad de aparición de llave (%)
points = 0  # Puntuación inicial del jugador
cantidad_enemigos = 5  # Cantidad de enemigos por tipo
velocidad_enemigos_1 = 1000  # Velocidad de movimiento para enemigos tipo 1
velocidad_enemigos_2 = 500  # Velocidad de movimiento para enemigos tipo 2
##########################################################################################################
def check_mute_state(): # Verificar si está muteado
    pygame.mixer.init()  # Inicializar el mezclador de audio de pygame
    if os.path.exists("mute_state.txt"):  # Verificar si el archivo de estado de silencio existe
        with open("mute_state.txt", "r+") as file:  # Abrir el archivo en modo lectura y escritura
            mute_state = file.read().strip()  # Leer el estado de silencio del archivo y eliminar espacios en blanco
            file.seek(0)  # Mover el cursor al principio del archivo
            file.truncate()  # Borrar el contenido del archivo
        if mute_state == "1":  # Si el estado de silencio es activado
            pygame.mixer.music.set_volume(0)  # Silenciar la música
            pygame.mixer.pause()  # Pausar todos los efectos de sonido
        else:  # Si el estado de silencio está desactivado
            pygame.mixer.music.set_volume(1)  # Restaurar volumen de la música
            pygame.mixer.unpause()  # Reanudar efectos de sonido pausados
    else:  # Si el archivo de estado de silencio no existe
        pygame.mixer.music.set_volume(1)  # Activar volumen de la música
        pygame.mixer.unpause()  # Activar efectos de sonido por defecto
check_mute_state()  # Llamar a la función para comprobar el estado de silencio al inicio
##########################################################################################################
#Música
pygame.init()  # Inicializar Pygame
pygame.mixer.init()  # Inicializar el mezclador de audio de Pygame
pygame.mixer.music.load('sounds/𝗱𝗼𝗿𝗶𝗮𝗻 𝗰𝗼𝗻𝗰𝗲𝗽𝘁 - 𝗵𝗶𝗱𝗲 (𝗰𝘀𝟬𝟭) (𝗺𝘆𝘀𝘁𝗲𝗿𝗶𝗼𝘂𝘀 𝗱𝘂𝗻𝗴𝗲𝗼𝗻_𝘀𝗹𝗼𝘄𝗲𝗱 + 𝗿𝗲𝘃𝗲𝗿𝗯).mp3')# Cargar y reproducir la música en bucle
pygame.mixer.music.play(-1)  # Reproducir la música en bucle (loop)
##########################################################################################################
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
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]
##########################################################################################################
#Ventana Principal
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}") # Establecer la geometría para centrar

ventana_juego = tk.Tk() # Crear la ventana principal del juego
ventana_juego.title("Bomberman Maze")  # Establecer el título de la ventana
ventana_juego.attributes('-fullscreen', True)  # Hacer la ventana fullscreen
ventana_juego.configure(bg='black')  # Establecer el color de fondo a negro
content_width = 1033 # Ancho
content_height = 760 # Alto

def close_window(event): # Cerrar ventana
    ventana_juego.destroy()
center_window(ventana_juego, content_width, content_height) #Centrar ventana
##########################################################################################################
#Parte Superior
canvas_superior = tk.Canvas(ventana_juego, width=1033, height=100, background="white")
canvas_superior.pack()

canvas_lifebar = tk.Canvas(canvas_superior, width=200, height=100, background="white")
canvas_lifebar.pack(side="left")

canvas_points = tk.Canvas(canvas_superior, width=400, height=100, background="white")
canvas_points.pack(side="left")

Font_Main = Font(family="Courier New", size=20, weight="bold")

time_label = tk.Label(canvas_points, text="TIME:0:00", font=Font_Main, fg="white", bg="black", padx=20)
time_label.pack(side="left")

points_label = tk.Label(canvas_points, text="POINTS: 00000", font=Font_Main, fg="black", bg="white", padx=20)
points_label.pack(side="left")

bombs_label = tk.Label(canvas_points, text=f"BOMBS: {cantidad_bombas}", font=Font_Main, fg="white", bg="black", padx=20)
bombs_label.pack(side="left")

key_label = tk.Label(canvas_points, text="KEY: NOT", font=Font_Main, fg="black", bg="white", padx=20)
key_label.pack(side="left")

def tiempo():
    global iniciar_tiempo
    tiempo_transcurrido = int(time.time() - iniciar_tiempo)
    minutos = tiempo_transcurrido // 60
    segundos = tiempo_transcurrido % 60
    
    time_label.config(text=f"TIME:{minutos}:{segundos:02d}")
    ventana_juego.after(1000, tiempo)  # Llama a esta función cada segundo
iniciar_tiempo = time.time() # Inicia el cronómetro al comenzar el juego
tiempo()

canvas_maze = tk.Canvas(ventana_juego, width=1000, height=683) # Canvas del maze
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
muro = muro.resize((tamaño, tamaño), Image.LANCZOS)  
muro = ImageTk.PhotoImage(muro)

cesped = Image.open("images/textures/cesped2.png")
cesped = cesped.resize((tamaño, tamaño), Image.LANCZOS) 
cesped = ImageTk.PhotoImage(cesped)

puerta_cesped = Image.open("images/textures/puertacesped.png")
puerta_cesped = puerta_cesped.resize((tamaño, tamaño), Image.LANCZOS) 
puerta_cesped = ImageTk.PhotoImage(puerta_cesped)

destructible = Image.open("images/textures/destructible3.png")
destructible = destructible.resize((tamaño, tamaño), Image.LANCZOS)
destructible_tk = ImageTk.PhotoImage(destructible)
##########################################################################################################
bloques_destructibles = [
    (1, 2), (2, 7), (4, 7), (6, 9), (8, 7), (6, 9), (8, 3), (4, 1), (5, 1), (12, 7), (14, 7), (4, 13), (8, 1), (10, 5), (12, 7), (11, 7), (8, 3), (7, 3), (14, 7), (16, 3), (8, 13), (10, 13), (10, 11), (14, 13), (15, 13), (13, 8), (12, 13), (15, 7), (15, 12), (16, 7), (15, 10), (14, 9), (13, 12), (14, 13), (10, 1), (10, 3), (13, 4), (16, 3), (15, 4), (16, 9), (17, 7), (21, 13), (21, 12), (20, 13), (17, 7), (16, 13), (11, 13), (11, 12), (1, 13), (1, 12), (1, 11), (2, 13), (3, 10), (1, 3), (3, 2), (3, 3), (1, 5), (21, 1), (20, 1), (15, 1), (3, 7), (21, 7), (21, 6), (21, 5), (21, 10), (21, 9), (20, 9), (19, 9), (17, 9), (17, 10), (18,11), (7, 6), (5, 6), (6, 7), (6, 5)]
def draw_maze_recursive(y=0, x=0):
    if y >= len(maze):  # Caso base: si llegamos al final del laberinto, terminamos la recursión
        return
    
    if maze[y][x] == 1:
        canvas_maze.create_image(x * tamaño, y * tamaño, anchor=tk.NW, image=muro)
    elif maze[y][x] == 2:
        canvas_maze.create_image(x * tamaño, y * tamaño, anchor=tk.NW, image=puerta_cesped)
    else:
        canvas_maze.create_image(x * tamaño, y * tamaño, anchor=tk.NW, image=cesped)
    
    if (x, y) in bloques_destructibles:
        canvas_maze.create_image(x * tamaño, y * tamaño, anchor=tk.NW, image=destructible_tk, tags=f"bloque_destructible_{x}_{y}")
    
    siguiente_x = x + 1
    siguiente_y = y
    if siguiente_x >= len(maze[y]):
        siguiente_x = 0
        siguiente_y = y + 1
    
    draw_maze_recursive(siguiente_y, siguiente_x)
draw_maze_recursive()

def encontrar_posicion_inicial():
  return tamaño, tamaño
posicion_inicial = encontrar_posicion_inicial()
##########################################################################################################
# Movimiento del Personaje
def iniciar_juego():
    global posicion_x_jugador, posicion_y_jugador, skin_tk, skin, skin_id, skin_seleccionada
    with open("skin_seleccionada.txt", "r") as file:
        skin_seleccionada = file.readline()

    posicion_x_jugador = posicion_inicial[0]
    posicion_y_jugador = posicion_inicial[1]

    ruta_imagen = f"images/skin1 - copia/{skin_seleccionada} frente.png"

    skin = Image.open(ruta_imagen)
    skin = skin.resize((tamaño, tamaño), Image.LANCZOS)
    skin_tk = ImageTk.PhotoImage(skin)
    skin_id = canvas_maze.create_image(posicion_x_jugador, posicion_y_jugador, anchor="nw", image=skin_tk)
iniciar_juego()

def subir(event):
    global posicion_x_jugador, posicion_y_jugador, skin_tk, skin, skin_seleccionada
    mueve_y = posicion_y_jugador - tamaño  # Calcula la nueva posición en el eje Y restando el tamaño de la casilla
    if mueve_y >= 0 and maze[mueve_y // tamaño][posicion_x_jugador // tamaño] == 0 and not verificar_colision_bloques_destructibles_recursivo(posicion_x_jugador, mueve_y):
        posicion_y_jugador = mueve_y  # Actualiza la posición Y del jugador
        canvas_maze.coords(skin_id, posicion_x_jugador, posicion_y_jugador)  # Actualiza las coordenadas del jugador en el lienzo
        if verificar_colision_con_enemigos_recursivo(posicion_x_jugador, posicion_y_jugador):  # Verifica colisión con enemigos
            return
        skin = Image.open(f"images/skin1 - copia/{skin_seleccionada} atras.png")  # Carga la imagen del jugador mirando hacia atrás
        skin = skin.resize((tamaño, tamaño), Image.LANCZOS)  # Redimensiona la imagen del jugador
        skin_tk = ImageTk.PhotoImage(skin)  # Convierte la imagen en formato Tkinter
        canvas_maze.itemconfig(skin_id, image=skin_tk)  # Actualiza la imagen del jugador en el lienzo

def bajar(event):
    global posicion_x_jugador, posicion_y_jugador, skin_tk, skin, skin_seleccionada
    mueve_y = posicion_y_jugador + tamaño  # Calcula la nueva posición en el eje Y sumando el tamaño de la casilla
    if mueve_y < len(maze) * tamaño and maze[mueve_y // tamaño][posicion_x_jugador // tamaño] == 0 and not verificar_colision_bloques_destructibles_recursivo(posicion_x_jugador, mueve_y):
        posicion_y_jugador = mueve_y  # Actualiza la posición Y del jugador
        canvas_maze.coords(skin_id, posicion_x_jugador, posicion_y_jugador)  # Actualiza las coordenadas del jugador en el lienzo
        if verificar_colision_con_enemigos_recursivo(posicion_x_jugador, posicion_y_jugador):  # Verifica colisión con enemigos
            return
        skin = Image.open(f"images/skin1 - copia/{skin_seleccionada} frente.png")  # Carga la imagen del jugador mirando hacia adelante
        skin = skin.resize((tamaño, tamaño), Image.LANCZOS)  # Redimensiona la imagen del jugador
        skin_tk = ImageTk.PhotoImage(skin)  # Convierte la imagen en formato Tkinter
        canvas_maze.itemconfig(skin_id, image=skin_tk)  # Actualiza la imagen del jugador en el lienzo

def izquierda(event):
    global posicion_x_jugador, posicion_y_jugador, skin_tk, skin, skin_seleccionada
    mueve_x = posicion_x_jugador - tamaño  # Calcula la nueva posición en el eje X restando el tamaño de la casilla
    if mueve_x >= 0 and maze[posicion_y_jugador // tamaño][mueve_x // tamaño] == 0 and not verificar_colision_bloques_destructibles_recursivo(mueve_x, posicion_y_jugador):
        posicion_x_jugador = mueve_x  # Actualiza la posición X del jugador
        canvas_maze.coords(skin_id, posicion_x_jugador, posicion_y_jugador)  # Actualiza las coordenadas del jugador en el lienzo
        if verificar_colision_con_enemigos_recursivo(posicion_x_jugador, posicion_y_jugador):  # Verifica colisión con enemigos
            return
        skin = Image.open(f"images/skin1 - copia/{skin_seleccionada} izq.png")  # Carga la imagen del jugador mirando hacia la izquierda
        skin = skin.resize((tamaño, tamaño), Image.LANCZOS)  # Redimensiona la imagen del jugador
        skin_tk = ImageTk.PhotoImage(skin)  # Convierte la imagen en formato Tkinter
        canvas_maze.itemconfig(skin_id, image=skin_tk)  # Actualiza la imagen del jugador en el lienzo

def derecha(event):
    global posicion_x_jugador, posicion_y_jugador, skin_tk, skin, skin_seleccionada
    mueve_x = posicion_x_jugador + tamaño  # Calcula la nueva posición en el eje X sumando el tamaño de la casilla
    if mueve_x < len(maze[0]) * tamaño and maze[posicion_y_jugador // tamaño][mueve_x // tamaño] == 0 and not verificar_colision_bloques_destructibles_recursivo(mueve_x, posicion_y_jugador):
        posicion_x_jugador = mueve_x  # Actualiza la posición X del jugador
        canvas_maze.coords(skin_id, posicion_x_jugador, posicion_y_jugador)  # Actualiza las coordenadas del jugador en el lienzo
        if verificar_colision_con_enemigos_recursivo(posicion_x_jugador, posicion_y_jugador):  # Verifica colisión con enemigos
            return
        skin = Image.open(f"images/skin1 - copia/{skin_seleccionada} der.png")  # Carga la imagen del jugador mirando hacia la derecha
        skin = skin.resize((tamaño, tamaño), Image.LANCZOS)  # Redimensiona la imagen del jugador
        skin_tk = ImageTk.PhotoImage(skin)  # Convierte la imagen en formato Tkinter
        canvas_maze.itemconfig(skin_id, image=skin_tk)  # Actualiza la imagen del jugador en el lienzo

def verificar_colision_bloques_destructibles_recursivo(mueve_x, mueve_y, index=0):
    if index >= len(bloques_destructibles):
        return False  # No hay colisión si no hay bloques destructibles restantes
    x, y = bloques_destructibles[index]
    if mueve_x == x * tamaño and mueve_y == y * tamaño:
        return True  # Hay colisión con un bloque destructible
    return verificar_colision_bloques_destructibles_recursivo(mueve_x, mueve_y, index + 1)  # Llama recursivamente para revisar el siguiente bloque destructible
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
        abrir_ventana_loss()
    vidas_restantes -= 1
##########################################################################################################
def abrir_ventana_loss():
    game_over_window = tk.Toplevel()
    game_over_window.attributes('-fullscreen', True)
    label_game_over = tk.Label(game_over_window, text="GAME OVER LOSS", font=("Arial", 24, "bold"))
    label_game_over.pack(expand=True)  # Expandir el Label para llenar la ventana
    
def abrir_ventana_win():
    game_over_win_window = tk.Toplevel()
    game_over_win_window.attributes('-fullscreen', True)
    label_game_over = tk.Label(game_over_win_window, text="GAME OVER WIN", font=("Arial", 24, "bold"))
    label_game_over.pack(expand=True)  # Expandir el Label para llenar la ventana
##########################################################################################################
#Enemigos
enemigos_ids = []
enemigo_image = Image.open("images/enemigo1.png")
enemigo_image = enemigo_image.resize((tamaño, tamaño), Image.LANCZOS)
enemigo_image_tk = ImageTk.PhotoImage(enemigo_image)

enemigo_image2 = Image.open("images/enemigo2.png")
enemigo_image2 = enemigo_image2.resize((tamaño, tamaño), Image.LANCZOS)
enemigo_image2_tk = ImageTk.PhotoImage(enemigo_image2)

def generar_enemigos(cantidad_enemigos, enemigo_ids, enemigo_image_tk):
    if cantidad_enemigos == 0:
        return
    while True:
        enemigo_x = random.randint(0, len(maze[0]) - 1)
        enemigo_y = random.randint(0, len(maze) - 1)
        if maze[enemigo_y][enemigo_x] == 0:
            break
    enemigo_id = canvas_maze.create_image(enemigo_x * tamaño, enemigo_y * tamaño, anchor='nw', image=enemigo_image_tk)
    enemigo_ids.append(enemigo_id)
    generar_enemigos(cantidad_enemigos - 1, enemigo_ids, enemigo_image_tk)

enemigo1_ids = []
generar_enemigos(cantidad_enemigos, enemigo1_ids, enemigo_image_tk)

enemigo2_ids = []
generar_enemigos(cantidad_enemigos, enemigo2_ids, enemigo_image2_tk)

def mover_enemigos_tipo1_recursivo(index=0):
    if index >= len(enemigo1_ids):
        ventana_juego.after(velocidad_enemigos_1, mover_enemigos_tipo1_recursivo)
        return

    enemigo_id = enemigo1_ids[index]
    enemigo_x, enemigo_y = canvas_maze.coords(enemigo_id)

    direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])

    if direccion == "arriba":
        nueva_y = enemigo_y - tamaño
        if nueva_y >= 0 and maze[int(nueva_y / tamaño)][int(enemigo_x / tamaño)] == 0:
            canvas_maze.move(enemigo_id, 0, -tamaño)
    elif direccion == "abajo":
        nueva_y = enemigo_y + tamaño
        if nueva_y < len(maze) * tamaño and maze[int(nueva_y / tamaño)][int(enemigo_x / tamaño)] == 0:
            canvas_maze.move(enemigo_id, 0, tamaño)
    elif direccion == "izquierda":
        nueva_x = enemigo_x - tamaño
        if nueva_x >= 0 and maze[int(enemigo_y / tamaño)][int(nueva_x / tamaño)] == 0:
            canvas_maze.move(enemigo_id, -tamaño, 0)
    elif direccion == "derecha":
        nueva_x = enemigo_x + tamaño
        if nueva_x < len(maze[0]) * tamaño and maze[int(enemigo_y / tamaño)][int(nueva_x / tamaño)] == 0:
            canvas_maze.move(enemigo_id, tamaño, 0)

    mover_enemigos_tipo1_recursivo(index + 1)

def mover_enemigos_tipo2_recursivo(index=0):
    if index >= len(enemigo2_ids):
        ventana_juego.after(velocidad_enemigos_2, mover_enemigos_tipo2_recursivo)
        return

    enemigo_id = enemigo2_ids[index]
    enemigo_x, enemigo_y = canvas_maze.coords(enemigo_id)

    direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])

    if direccion == "arriba":
        nueva_y = enemigo_y - tamaño
        if nueva_y >= 0 and maze[int(nueva_y / tamaño)][int(enemigo_x / tamaño)] == 0 and not verificar_colision_bloques_destructibles_recursivo(enemigo_x, nueva_y):
            canvas_maze.move(enemigo_id, 0, -tamaño)
    elif direccion == "abajo":
        nueva_y = enemigo_y + tamaño
        if nueva_y < len(maze) * tamaño and maze[int(nueva_y / tamaño)][int(enemigo_x / tamaño)] == 0 and not verificar_colision_bloques_destructibles_recursivo(enemigo_x, nueva_y):
            canvas_maze.move(enemigo_id, 0, tamaño)
    elif direccion == "izquierda":
        nueva_x = enemigo_x - tamaño
        if nueva_x >= 0 and maze[int(enemigo_y / tamaño)][int(nueva_x / tamaño)] == 0 and not verificar_colision_bloques_destructibles_recursivo(nueva_x, enemigo_y):
            canvas_maze.move(enemigo_id, -tamaño, 0)
    elif direccion == "derecha":
        nueva_x = enemigo_x + tamaño
        if nueva_x < len(maze[0]) * tamaño and maze[int(enemigo_y / tamaño)][int(nueva_x / tamaño)] == 0 and not verificar_colision_bloques_destructibles_recursivo(nueva_x, enemigo_y):
            canvas_maze.move(enemigo_id, tamaño, 0)

    mover_enemigos_tipo2_recursivo(index + 1)

ventana_juego.after(velocidad_enemigos_1, mover_enemigos_tipo1_recursivo)
ventana_juego.after(velocidad_enemigos_2, mover_enemigos_tipo2_recursivo)

def verificar_colision_con_enemigos_recursivo(posicion_x_jugador, posicion_y_jugador, index=0):
    global enemigo1_ids, enemigo2_ids
    enemigos_ids = enemigo1_ids + enemigo2_ids
    if index >= len(enemigos_ids):
        return False  # No hay más enemigos que verificar, no hay colisión
    enemigo_id = enemigos_ids[index]
    enemigo_x, enemigo_y = canvas_maze.coords(enemigo_id)
    
    if abs(posicion_x_jugador - enemigo_x) < tamaño and abs(posicion_y_jugador - enemigo_y) < tamaño:
        quitar_vida()
        return True
    return verificar_colision_con_enemigos_recursivo(posicion_x_jugador, posicion_y_jugador, index + 1)
##########################################################################################################
#Bomba
explosion_tamaño = 75
bomba_image = PhotoImage(file="images/bomba.png")
bomba_image = bomba_image.subsample(int(bomba_image.width() / tamaño), int(bomba_image.height() / tamaño))  # Redimensionar la imagen
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
        
        explosion_x = bomba_x
        explosion_y = bomba_y
        
        if index == 0:
            if abs(posicion_x_jugador - explosion_x) <= explosion_tamaño and abs(posicion_y_jugador - explosion_y) <= explosion_tamaño:
                quitar_vida()
        destruir_bloques_destructibles(bomba_x // tamaño, bomba_y // tamaño, explosion_tamaño)
        eliminar_enemigos_recursivo(bomba_x, bomba_y)
        ventana_juego.after(100, lambda: mostrar_frames_explosion(frames, index + 1, x-10, y-10, bomba_x, bomba_y))

def eliminar_enemigos_recursivo(bomba_x, bomba_y, index=0):
    global enemigo1_ids, enemigo2_ids
    if index < len(enemigo1_ids):
        enemigo_id = enemigo1_ids[index]
        enemigo_x, enemigo_y = canvas_maze.coords(enemigo_id)

        if abs(enemigo_x - bomba_x) <= explosion_tamaño and abs(enemigo_y - bomba_y) <= explosion_tamaño:
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
            canvas_maze.delete(enemigo_id)
            aumentar_puntos(500)
            enemigo2_ids.pop(index - len(enemigo1_ids))  # Ajuste del índice para el segundo tipo de enemigo
            eliminar_enemigos_recursivo(bomba_x, bomba_y, index)  # Llamada recursiva con el mismo índice para procesar el siguiente enemigo
        else:
            eliminar_enemigos_recursivo(bomba_x, bomba_y, index + 1)  # Llamada recursiva con el siguiente índice

def colocar_bomba(event):
    global bomba_colocada, bomba_x, bomba_y, cantidad_bombas
    if not bomba_colocada:
        bomba_x = posicion_x_jugador // tamaño
        bomba_y = posicion_y_jugador // tamaño
        canvas_maze.create_image(bomba_x * tamaño, bomba_y * tamaño, anchor="nw", image=bomba_image, tags=("bomba", "elemento"))
        bomba_colocada = True
        ventana_juego.after(tiempo_explosion * 1000, explotar_bomba_recursivo)
        bomba_colocada = True
        cantidad_bombas -= 1  # Disminuir la cantidad de bombas disponibles
        bombs_label.config(text=f"BOMBS: {cantidad_bombas}")
        if cantidad_bombas<=9:
            bombs_label.config(text=f"BOMBS: 0{cantidad_bombas}")
        if cantidad_bombas == 0:  # Verificar si la cantidad de bombas es cero
            abrir_ventana_loss()

def explotar_bomba_recursivo():
    global bomba_colocada, bomba_x, bomba_y
    canvas_maze.delete("bomba")
    bomba_colocada = False
    x = bomba_x * tamaño
    y = bomba_y * tamaño
    mostrar_frames_explosion(frames_explosion_resized, 0, x, y, x, y)
##########################################################################################################
bloques_destructibles_destruidos = []

def destruir_bloques_destructibles(bomba_x, bomba_y, explosion_tamaño):
    global bloques_destructibles, bloques_destructibles_destruidos, maze, points

    def destruir_bloque_recursivo(index=0):
        if index >= len(bloques_destructibles):
            return
        x, y = bloques_destructibles[index]
        if abs(x - bomba_x) <= explosion_tamaño // tamaño and abs(y - bomba_y) <= explosion_tamaño // tamaño:
            canvas_maze.delete(f"bloque_destructible_{x}_{y}")
            maze[y][x] = 0
            bloques_destructibles_destruidos.append((x, y))
            bloques_destructibles.pop(index)
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
#Generación de Llave
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
        key_id = canvas_maze.create_image(key_x * tamaño, key_y * tamaño, anchor=tk.NW, image=key_image, tags=("llave"))
        canvas_maze.tag_lower(key_id, f"bloque_destructible_{key_x}_{key_y}")
    else:
        key_x = key_y = -1  # Restablecer las coordenadas de la llave si no se encuentra una posición válida

def obtener_llave(event):
    global key_x, key_y, posicion_x_jugador, posicion_y_jugador, key_label, key_obtained, key_id
    if key_x != -1 and key_y != -1 and posicion_x_jugador == key_x * tamaño and posicion_y_jugador == key_y * tamaño:
        key_label.config(text="KEY: YES")
        canvas_maze.delete(key_id)  # Ocultar la imagen de la llave
        key_obtained = True
        aumentar_puntos(500)

key_image = Image.open("images/objs/keyicon.png")
key_image = key_image.resize((tamaño, tamaño), Image.LANCZOS)
key_image_tk = ImageTk.PhotoImage(key_image)

generar_llave_aleatoria(maze, key_image_tk, bloques_destructibles)
##########################################################################################################
# Puerta
door_location = (12, 13)
door_image = Image.open("images/objs/door_closed.png")
door_image = door_image.resize((tamaño, tamaño), Image.LANCZOS)
door_image_tk = ImageTk.PhotoImage(door_image)
door_id = canvas_maze.create_image(door_location[0] * tamaño, door_location[1] * tamaño, anchor=tk.NW, image=door_image_tk, tags=("puerta"))
canvas_maze.itemconfig(door_id, state="hidden")

def abrir_puerta(event):
    global key_obtained, door_location, door_id, nivel_actual
    if key_obtained and posicion_x_jugador // tamaño == door_location[0] and posicion_y_jugador // tamaño == door_location[1]:
        canvas_maze.delete(door_id)
        if nivel_actual == 1:
            nivel_actual = 2
            reiniciar_juego(nivel_actual)
        elif nivel_actual == 2:
            nivel_actual = 3
            reiniciar_juego(nivel_actual)
        elif nivel_actual == 3:
            abrir_ventana_win()
            aumentar_puntos(1000)
##########################################################################################################
#Controles
ventana_juego.bind("k", abrir_puerta)
ventana_juego.bind("j", obtener_llave)
ventana_juego.bind("K", abrir_puerta)
ventana_juego.bind("J", obtener_llave)
ventana_juego.bind('<Escape>', close_window)
ventana_juego.bind("<space>", colocar_bomba)
ventana_juego.bind("<Up>", subir)
ventana_juego.bind("<Down>", bajar)
ventana_juego.bind("<Left>", izquierda)
ventana_juego.bind("<Right>", derecha)
ventana_juego.bind("w", subir)
ventana_juego.bind("s", bajar)
ventana_juego.bind("a", izquierda)
ventana_juego.bind("d", derecha)
ventana_juego.bind("W", subir)
ventana_juego.bind("S", bajar)
ventana_juego.bind("A", izquierda)
ventana_juego.bind("D", derecha)
##########################################################################################################
#Ranking
def guardar_puntos_totales(puntos_finales):
    with open('puntos.txt', 'w') as file:
        file.write(str(puntos_finales))
##########################################################################################################
def eliminar_enemigos(enemigo1_index=0, enemigo2_index=0):
    global enemigo1_ids, enemigo2_ids
    if enemigo1_index < len(enemigo1_ids):
        enemigo_id = enemigo1_ids[enemigo1_index]
        canvas_maze.delete(enemigo_id)
        eliminar_enemigos(enemigo1_index + 1, enemigo2_index)
    elif enemigo2_index < len(enemigo2_ids):
        enemigo_id = enemigo2_ids[enemigo2_index]
        canvas_maze.delete(enemigo_id)
        eliminar_enemigos(enemigo1_index, enemigo2_index + 1)
    else:
        enemigo1_ids = []
        enemigo2_ids = []

def reiniciar_juego(nivel):
    global posicion_x_jugador, posicion_y_jugador, cantidad_enemigos, probabilidad_llave, door_location, skin_id, bloques_destructibles, maze
    if nivel_actual == 2:
        posicion_x_jugador, posicion_y_jugador = encontrar_posicion_inicial()
        generar_llave_aleatoria(maze, key_image_tk, bloques_destructibles)
        skin_id = canvas_maze.create_image(posicion_x_jugador, posicion_y_jugador, anchor="nw", image=skin_tk)
        key_label.config(text="KEY: NOT")
        canvas_maze.delete("bloque_destructible")
        definir_bloques_destructibles_recursivo(nivel=2)
        cantidad_bombas = 30
        bombs_label.config(text=f"BOMBS: {cantidad_bombas}")
        eliminar_enemigos()
        cantidad_enemigos = 7  # Cambia este valor por la cantidad deseada de enemigos para el nivel 2
        generar_enemigos(cantidad_enemigos, enemigo1_ids, enemigo_image_tk)
        generar_enemigos(cantidad_enemigos, enemigo2_ids, enemigo_image2_tk)

    elif nivel_actual == 3:
        posicion_x_jugador, posicion_y_jugador = encontrar_posicion_inicial()
        generar_llave_aleatoria(maze, key_image_tk, bloques_destructibles)
        skin_id = canvas_maze.create_image(posicion_x_jugador, posicion_y_jugador, anchor="nw", image=skin_tk)
        key_label.config(text="KEY: NOT")
        canvas_maze.delete("bloque_destructible")
        definir_bloques_destructibles_recursivo(nivel=3)
        cantidad_bombas = 25
        bombs_label.config(text=f"BOMBS: {cantidad_bombas}")
        eliminar_enemigos()
        cantidad_enemigos = 10  # Cambia este valor por la cantidad deseada de enemigos para el nivel 3
        generar_enemigos(cantidad_enemigos, enemigo1_ids, enemigo_image_tk)
        generar_enemigos(cantidad_enemigos, enemigo2_ids, enemigo_image2_tk)

def definir_bloques_destructibles_recursivo(nivel, index=0, bloques_nivel=None):
    if bloques_nivel is None:
        if nivel == 2:
            bloques_nivel = [(1, 2), (2, 7), (4, 7), (6, 9), (8, 7), (6, 9), (8, 3), (4, 1), (5, 1), (12, 7), (14, 7), (4, 13), (8, 1), (10, 5), (12, 7), (11, 7), (8, 3), (7, 3), (14, 7), (16, 3), (8, 13), (10, 13), (10, 11), (14, 13), (15, 13), (13, 8), (12, 13), (15, 7), (15, 12), (16, 7), (15, 10), (14, 9), (13, 12), (14, 13), (10, 1), (10, 3), (13, 4), (16, 3), (15, 4), (16, 9), (17, 7), (21, 13), (21, 12), (20, 13), (17, 7), (16, 13), (11, 13), (11, 12), (1, 13), (1, 12), (1, 11), (2, 13), (3, 10), (1, 3), (3, 2), (3, 3), (1, 5), (21, 1), (20, 1), (15, 1), (3, 7), (21, 7), (21, 6), (21, 5), (21, 10), (21, 9), (20, 9), (19, 9), (17, 9), (17, 10), (18,11), (7, 6), (5, 6), (6, 7), (6, 5), (6, 11), (6, 13), (7, 12), (5, 12)]
        elif nivel == 3:
            bloques_nivel = [(1, 2), (2, 7), (4, 7), (6, 9), (8, 7), (6, 9), (8, 3), (4, 1), (5, 1), (12, 7), (14, 7), (4, 13), (8, 1), (10, 5), (12, 7), (11, 7), (8, 3), (7, 3), (14, 7), (16, 3), (8, 13), (10, 13), (10, 11), (14, 13), (15, 13), (13, 8), (12, 13), (15, 7), (15, 12), (16, 7), (15, 10), (14, 9), (13, 12), (14, 13), (10, 1), (10, 3), (13, 4), (16, 3), (15, 4), (16, 9), (17, 7), (21, 13), (21, 12), (20, 13), (17, 7), (16, 13), (11, 13), (11, 12), (1, 13), (1, 12), (1, 11), (2, 13), (3, 10), (1, 3), (3, 2), (3, 3), (1, 5), (21, 1), (20, 1), (15, 1), (3, 7), (21, 7), (21, 6), (21, 5), (21, 10), (21, 9), (20, 9), (19, 9), (17, 9), (17, 10), (18,11), (7, 6), (5, 6), (6, 7), (6, 5), (6, 11), (6, 13), (7, 12), (5, 12), (8, 9), (8, 11), (7, 10), (9, 10), (18, 5), (18, 3), (17, 4), (19, 4)]
    if index < len(bloques_nivel):
        x, y = bloques_nivel[index]
        canvas_maze.delete(f"bloque_destructible_{x}_{y}")
        canvas_maze.create_image(x * tamaño, y * tamaño, anchor=tk.NW, image=destructible_tk, tags=f"bloque_destructible_{x}_{y}")
        bloques_destructibles.append((x, y))
        definir_bloques_destructibles_recursivo(nivel, index + 1, bloques_nivel)
    else:
        return

nivel_actual = 1
reiniciar_juego(nivel_actual)
##########################################################################################################

ventana_juego.mainloop()
 