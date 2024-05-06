from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.font import Font
import os
import pygame
import random

# Cargar las imágenes de los frames
cara_frames = []
for i in range(1, 7):
    frame_path = os.path.join('frames', f'{i}.png')
    frame_image = ImageTk.PhotoImage(file=frame_path)
    cara_frames.append(frame_image)

cruz_frames = []
for i in range(7, 12):
    frame_path = os.path.join('frames', f'{i}.png')
    frame_image = ImageTk.PhotoImage(file=frame_path)
    cruz_frames.append(frame_image)

# Elegir aleatoriamente cara o cruz
frames = random.choice([cara_frames, cruz_frames])

def animar_moneda(frame_index):
    global canvas, frames
    
    # Mostrar el frame actual en el canvas
    canvas.create_image(150, 150, image=frames[frame_index])
    
    # Avanzar al siguiente frame después de un pequeño retraso
    frame_index += 1
    if frame_index == len(frames):
        frame_index = 0
    root.after(50, animar_moneda, frame_index)

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Iniciar la animación
animar_moneda(0)

root.mainloop()