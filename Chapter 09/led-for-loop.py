#import libraries
from gpiozero import LED
from time import sleep

#define the LED
led = LED(17)

# Blink the LED four times
for i in range(1, 5):
    led.on()
    sleep(1)
    led.off()
    sleep(1)