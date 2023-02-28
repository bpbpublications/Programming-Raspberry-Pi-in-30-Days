#import libraries
from gpiozero import PWMLED

# define LED
led = PWMLED(17)

# Loop through the various brightness levels
while True:
    led.value = 0 # Off
    sleep(1)
    led.value = 0.5 # Half bright
    sleep(1)
    led.value = 1 # Fully bright
    sleep(1)