import machine
import time
import random
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




 