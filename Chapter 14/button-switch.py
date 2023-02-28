from machine import Pin
from utime import sleep

button_one = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_two = Pin(12, Pin.IN, Pin.PULL_UP)

while True:
    if button_one.value() == 1:
        print("up")
    if button_two.value() == 0:
        print("down")
    sleep(0.25)
