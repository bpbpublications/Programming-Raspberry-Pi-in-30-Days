from machine import Pin
from utime import sleep

red = Pin(15, Pin.OUT)
green = Pin(13, Pin.OUT)
yellow = Pin(11, Pin.OUT)

red.value(0)
green.value(0)
yellow.value(0)

button_two = Pin(12, Pin.IN, Pin.PULL_UP)

while True:
    if button_two.value() == 0:
        red.value(1)
        green.value(0)
        yellow.value(0)
        sleep(1)
        yellow.value(1)
        red.value(0)
        green.value(0)
        sleep(1)
        green.value(1)
        red.value(0)
        yellow.value(0)
        sleep(1)
        red.value(0)
        yellow.value(0)
        green.value(0)
