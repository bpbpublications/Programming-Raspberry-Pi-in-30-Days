from machine import Pin
from utime import sleep

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

forward()
sleep(1)
backward()
sleep(1)
stop()
