from machine import Pin, PWM, ADC
from utime import sleep

pot = ADC(Pin(26))

servo = PWM(Pin(0))

while True:
    value = int(1350 + (pot.read_u16()/9.57))
    servo.duty_u16(value)
    sleep(2)
