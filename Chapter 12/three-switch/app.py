#import libraries
from flask import Flask, render_template, request
from gpiozero import LEDBoard

#Define the lights
rooms = LEDBoard(17, 27, 22)

#define the app
app = Flask(__name__)

#Define the home route
@app.route('/')
def home():
    return render_template('lights.html')

#Add the functions for the LEDs
@app.route('/kitchen')
def kitchen():
    rooms.value = (1, 0, 0)
    return render_template('lights.html')

@app.route('/livingroom')
def livingroom():
    rooms.value = (0, 1, 0)
    return render_template('lights.html')

@app.route('/bedroom')
def bedroom():
    rooms.value = (0, 0, 1)
    return render_template('lights.html')

@app.route('/off')
def off():
    rooms.off()
    return render_template('lights.html')

#Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0')