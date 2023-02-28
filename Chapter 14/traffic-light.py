from machine import Pin
from utime import sleep

red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)

while True:
    red.value(1)
    yellow.value(0)
    green.value(0)
    sleep(1)
    red.value(0)
    yellow.value(1)
    green.value(0)
    sleep(1)
    red.value(0)
    yellow.value(0)
    green.value(1)
    sleep(1)
