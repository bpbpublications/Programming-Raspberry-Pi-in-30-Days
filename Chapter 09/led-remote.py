#import libraries
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import LED
from time import sleep

# Define our factory
factory = PiGPIOFactory(host='192.168.0.12')

# Define the LED
led = LED(17, pin_factory=factory)

# Blink the LED indefinitely
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)