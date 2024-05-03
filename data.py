import machine
import time
import random
import utime
from machine import Pin
#LEDS
LED1 = Pin(13, Pin.OUT)
def Leds():
    LED1.on()
    time.sleep(1)
    LED1.off()
    
#############################################################################
paleta1 = machine.Pin(7,machine.Pin.IN)
paleta2 = machine.Pin(8,machine.Pin.IN)
paleta3 = machine.Pin(9,machine.Pin.IN)
paleta4 = machine.Pin(10,machine.Pin.IN)
paleta5 = machine.Pin(11,machine.Pin.IN)
paleta6 = machine.Pin(12,machine.Pin.IN)
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
while True:
    print(paleta1.value())
    if paleta1.value() == 1:
        print("paleta1")
        print("-")
        activar_buzzer()
        Leds()
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
###########################################################################

