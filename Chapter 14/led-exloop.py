from machine import Pin
from utime import sleep

led_external = Pin(15, Pin.OUT)

for x in range(4):
    led_external.toggle()
    sleep(1)
