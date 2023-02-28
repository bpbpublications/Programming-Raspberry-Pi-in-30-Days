from machine import PWM, ADC, Pin
from utime import sleep

red = PWM(Pin(15))
pot = ADC(26)

red.freq(1000)

while True:
    red.duty_u16(pot.read_u16())
