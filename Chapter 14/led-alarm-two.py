from machine import Pin
from utime import sleep_ms, sleep

pir = Pin(14, Pin.IN, Pin.PULL_DOWN)
green = Pin(15, Pin.OUT)
red = Pin(13, Pin.OUT)

def pir_handler(pin):
    sleep_ms(100)
    if pin.value():
        print("motion detected")
        for i in range(4):
            red.toggle()
            sleep(1)

pir.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

while True:
    green.toggle()
    sleep(1)
