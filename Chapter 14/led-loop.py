from machine import Pin
from utime import sleep

led_onboard = Pin(25, Pin.OUT)

for x in range(2):
    led_onboard.value(1)
    sleep(1)
    led_onboard.value(0)
    sleep(1)
