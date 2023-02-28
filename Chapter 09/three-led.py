#import libraries
from gpiozero import LEDBoard
from time import sleep
from signal import pause

#define our LEDs
lights = LEDBoard(17, 27, 22)

#Blink the LEDs one at a time
lights.value = (1, 0, 0)
sleep(1)
lights.value = (0, 1, 0)
sleep(1)
lights.value = (0, 0, 1)
sleep(1)
lights.off()

#Keep the script running
pause()
