#import libraries
from gpiozero import LED
from time import sleep

# Define the LED
led = LED(17)

# Blink the LED indefinitely
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)