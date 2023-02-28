from machine import Pin
from utime import sleep_ms

pir = Pin(14, Pin.IN, Pin.PULL_DOWN)

def pir_handler(pin):
    sleep_ms(100)
    if pin.value():
        print("motion detected")
        
pir.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

