from machine import Pin, PWM
from utime import sleep

servo = PWM(Pin(0))

servo.freq(50)

while True:
    servo.duty_u16(1350)
    sleep(2)
    servo.duty_u16(8200)
    sleep(2)
