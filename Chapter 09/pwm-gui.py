#import libraries
from guizero import App, Slider, Text
from gpiozero import PWMLED

#Define the LED
led = PWMLED(17)

#Define the function that will connect to the slider
def ledlevel(slider_value):
    led.value = int(slider_value) / 10

#Define the app
app = App(title="LED PWM")
app.bg = "#44f141"

#Add title text
message = Text(app, text="LED PWM Control")
message.text_size = 20

#Add the slider
pwm_slider = Slider(app, start=0, end=10, command=ledlevel)
pwm_slider.bg = "#f1f141"

#display the app
app.display()