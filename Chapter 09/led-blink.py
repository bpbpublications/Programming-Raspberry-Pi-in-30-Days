#import libraries
from gpiozero import LED
from time import sleep

# Define our led
led = LED(17)

# Blink led
led.on()
sleep(1)
led.off()