import machine
import time
import random
from machine import Pin, ADC
import utime
import framebuf
#############################################################################
#LEDS
led = machine.Pin(16,machine.Pin.OUT)
#############################################################################
paleta1 = machine.Pin(7,machine.Pin.IN)
paleta2 = machine.Pin(8,machine.Pin.IN)
paleta3 = machine.Pin(9,machine.Pin.IN)
paleta4 = machine.Pin(10,machine.Pin.IN)
paleta5 = machine.Pin(11,machine.Pin.IN)
paleta6 = machine.Pin(12,machine.Pin.IN)

paletas = [paleta1, paleta2, paleta3, paleta4, paleta5, paleta6]
#############################################################################
#Pines
potenciometro = machine.ADC(26)
boton = machine.Pin(13, machine.Pin.IN)
buzzer = machine.Pin(21, machine.Pin.OUT)
#############################################################################
#Buzzer
def activar_buzzer():
    buzzer.on()
    time.sleep(0.1)
    buzzer.off()
#############################################################################
#Paletas
while True:
    if paleta1.value() == 1:
        print("paleta1")
        print("-")
        activar_buzzer()
    if paleta2.value() == 1:
        print("paleta2")
        print("-")
        activar_buzzer()
    if paleta3.value() == 1:
        print("paleta3")
        print("-")
        activar_buzzer()
    if paleta4.value() == 1:
        print("paleta4")
        print("-")
        activar_buzzer()
    if paleta5.value() == 1:
        print("paleta5")
        print("-")
        activar_buzzer()
    if paleta6.value() == 1:
        print("paleta6")
        print("-")
        activar_buzzer()
    time.sleep(0.1)
#############################################################################
while True:
    paleta_seleccionada = random.choice(paletas)
    if paleta_seleccionada.value() == 1:
        print("Paleta seleccionada:", paletas.index(paleta_seleccionada) + 1)
        print("-")
        activar_buzzer()
    time.sleep(10)



# Configurar los pines GPIO para los botones y los LEDs esto puede variar
button_pins = [15, 14, 13, 12, 11, 10]  # Pines para los botones
led_pins = [9, 8, 7, 6, 5, 4]  # Pines para los LEDs
potentiometer_pin = 26
select_button_pin = 16

potentiometer = ADC(Pin(potentiometer_pin))
select_button = Pin(select_button_pin, Pin.IN, Pin.PULL_UP)

# Configurar los pines como entradas para los botones
buttons = [Pin(pin, Pin.IN, Pin.PULL_UP) for pin in button_pins]
# Configurar los pines como salidas para los LEDs
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

# Definir los personajes (jugadores y porteros)
players = ["Jugador 1", "Jugador 2", "Jugador 3", "Jugador 4", "Jugador 5", "Jugador 6", "Jugador 7", "Jugador 8", "Jugador 9"]
teams = ["Equipo1", "Equipo2", "Equipo3"]
selected_player = 0


"""def load_player_image(player_index):
    team_index = player_index // 3  # Índice del equipo
    player_number = player_index % 3 + 1  # Número del jugador dentro del equipo
    image_path = f"Jugadores/{teams[team_index]}/Jugador{player_number}.png"

    # Cargar la imagen del jugador y mostrarla en pantalla
    with open(image_path, "rb") as f:
        image = framebuf.FrameBuf(f.read(), width, height, framebuf.RGB565)
    display.blit(image, 0, 0)"""


# Función para manejar los botones y encender/apagar los LEDs
def handle_buttons():
    for i in range(6):
        if not buttons[i].value():
            leds[i].value(not leds[i].value())
            utime.sleep(0.2)


# Función para seleccionar el jugador
def select_player():
    global selected_player
    if not select_button.value():
        potentiometer_value = potentiometer.read_u16()
        selected_player = int(potentiometer_value / 7324)  # 7324 valor max de potenciometro de 5k cambiar si es de menos
        print(f"Jugador seleccionado: {players[selected_player]}")
        load_player_image(selected_player)

while True:
    handle_buttons()
    select_player()
    utime.sleep(0.1)  # pausa para no sobrecargar el procesador


 