import machine
import time
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
#############################################################################
#Potenciometro y botón
potenciometro = machine.ADC(26)
boton = machine.Pin(13, machine.Pin.IN)
#############################################################################
#Paletas
while True:
    if paleta1.value() == 1:
        print("paleta1")
        print("-")
    if paleta2.value() == 1:
        print("paleta2")
        print("-")
    if paleta3.value() == 1:
        print("paleta3")
        print("-")
    if paleta4.value() == 1:
        print("paleta4")
        print("-")
    if paleta5.value() == 1:
        print("paleta5")
        print("-")
    if paleta6.value() == 1:
        print("paleta6")
        print("-")
    time.sleep(0.5)
#############################################################################
#Potenciometro 

#############################################################################




