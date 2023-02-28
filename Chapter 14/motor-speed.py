from machine import Pin, ADC, PWM
from utime import sleep

red = Pin(12, Pin.OUT)
yellow = Pin(13, Pin.OUT)
green = Pin(14, Pin.OUT)

button_down = Pin(15, Pin.IN, Pin.PULL_DOWN)
button_up = Pin(16, Pin.IN, Pin.PULL_UP)

en_1 = PWM(Pin(17))
in_1 = Pin(18, Pin.OUT)
in_2 = Pin(19, Pin.OUT)

pot = ADC(26)

def forward():
    in_1.value(1)
    in_2.value(0)

def backward():
    in_1.value(0)
    in_2.value(1)

def stop():
    in_1.value(0)
    in_2.value(0)

red.value(1)
green.value(0)
yellow.value(0)

en_1.freq(50)
stop()

while True:
    en_1.duty_u16(pot.read_u16())
    if button_down.value() == 1:
        forward()
        red.value(0)
        green.value(1)
        yellow.value(0)
    
    if button_up.value() == 0:
        backward()
        red.value(0)
        green.value(0)
        yellow.value(1)
        
    sleep(0.25)
