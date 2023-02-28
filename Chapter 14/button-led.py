from machine import Pin
from utime import sleep

red = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        red.value(1)
        sleep(2)
    red.value(0)
