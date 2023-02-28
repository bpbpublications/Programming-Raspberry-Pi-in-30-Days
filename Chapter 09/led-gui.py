#import libraries
from guizero import App, PushButton, Text
from gpiozero import LED

#Define the LED
led = LED(17)

#Define our functions

def ledon():
    led.on()

def ledoff():
    led.off()

#Define the app
app = App(title="LED Control")
app.bg = "#41f1f1"

#Add some text
message = Text(app, text="LED Button")
message.text_size = 20

#Define the button
button = PushButton(app, text="ON")
button.when_left_button_pressed = ledon
button.when_left_button_released = ledoff
button.text_size = 20
button.bg = "#f141ee"

#display app
app.display()