#import libraries
from flask import Flask, render_template, request
from gpiozero import LED

#define led
led = LED(17)

#define app
app = Flask(__name__)

#define home route
@app.route('/')
def home():
    return render_template('switch.html')

#define the on function
@app.route('/on')
def ledon():
    led.on()
    return render_template('switch.html')

#Define the off function
@app.route('/off')
def ledoff():
    led.off()
    return render_template('switch.html')
 
#Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0')