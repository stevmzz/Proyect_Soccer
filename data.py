import machine
import time
import random
import utime
from machine import Pin
import network
from machine import ADC, PWM
from time import sleep
#############################################################################
#Internet
ssid = "Philip Hoffman Cloco Clifford"
password = "3131313100000"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

running = True

while not wifi.isconnected():
    time.sleep(1)
print("Conexion establecida: ", wifi.ifconfig())

SERVER_IP = "192.168.43.149"
SERVER_PORT = 50000
#############################################################################
potenciometro = ADC(28)
#############################################################################

#LEDS
LED1 = Pin(27, Pin.OUT)
LED2 = Pin(26, Pin.OUT)
BOTON = Pin(5, Pin.IN, Pin.PULL_UP)

def control_leds():
    if BOTON.value() == 1:
        LED1.on()
        LED2.off()
    else:
        LED1.off()
        LED2.on()
control_leds()

LED_1 = Pin(15, Pin.OUT)
LED_2 = Pin(14, Pin.OUT)
LED_3 = Pin(16, Pin.OUT)
LED_4 = Pin(17, Pin.OUT)
LED_5 = Pin(13, Pin.OUT)
LED_6 = Pin(18, Pin.OUT)
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
buzzer = machine.Pin(21, machine.Pin.OUT)
#############################################################################
#Buzzer
def activar_buzzer():
    buzzer.on()
    time.sleep(0.1)
    buzzer.off()
#############################################################################
#Paletas
paleta_random = random.choice(paletas)
print(paleta_random)

while True:
    # Paleta aleatoria
    paleta_random = random.choice(paletas)
    print("Paleta aleatoria:", paleta_random)

    while True:
        if paleta_random.value() == 1:
            print("Ganaste con la paleta:", paleta_random)
            activar_buzzer()
            # Encender el LED correspondiente a la paleta aleatoria
            if paleta_random == paleta1:
                LED_1.on()
            elif paleta_random == paleta2:
                LED_2.on()
            elif paleta_random == paleta3:
                LED_3.on()
            elif paleta_random == paleta4:
                LED_4.on()
            elif paleta_random == paleta5:
                LED_5.on()
            elif paleta_random == paleta6:
                LED_6.on()
            utime.sleep(6)  # Esperar 6 segundos antes de apagar el LED
            LED_1.off()
            LED_2.off()
            LED_3.off()
            LED_4.off()
            LED_5.off()
            LED_6.off()
            break
    utime.sleep(3)  # Esperar 3 segundos antes de lanzar otra paleta aleatoria
###########################################################################

 