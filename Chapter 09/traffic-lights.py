#import libraries
from gpiozero import LEDBoard
from time import sleep

#define our LEDs
lights = LEDBoard(17, 27, 22)

#Blink the LEDs like a traffic stop
while True:
    lights.value = (1, 0, 0)
    sleep(10)
    lights.value = (0, 0, 1)
    sleep(20)
    lights.value = (0, 1, 0)
    sleep(5)

