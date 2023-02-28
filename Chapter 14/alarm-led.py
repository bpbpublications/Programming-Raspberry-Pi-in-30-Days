from machine import Pin
from utime import sleep, sleep_ms

pir = Pin(14, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT)

def pir_handler(pin):
    sleep_ms(100)
    if pin.value():
        print("motion detected")
        for i in range(4):
            led.toggle()
            sleep(1)
        
pir.irq(trigger=Pin.IRQ_RISING, hander=pir_handler)