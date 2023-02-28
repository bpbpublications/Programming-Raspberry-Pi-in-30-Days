from machine import Pin
from utime import sleep

button_one = Pin(13, Pin.IN, Pin.PULL_DOWN)
button_two = Pin(12, Pin.IN, Pin.PULL_UP)

in_1 = Pin(15, Pin.OUT)
in_2 = Pin(14, Pin.OUT)

def forward():
    in_1.value(1)
    in_2.value(0)
    
def backward():
    in_1.value(0)
    in_2.value(1)

def stop():
    in_1.value(0)
    in_2.value(0)

stop()

while True:
    if button_one.value() == 1:
        forward()
    if button_two.value() == 0:
        backward()
    sleep(.5)
    
