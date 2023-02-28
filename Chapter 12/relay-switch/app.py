#import libraries
from flask import Flask, render_template, request
from gpiozero import OutputDevice

#Define our Relays
relay_1 = OutputDevice(21)
relay_2 = OutputDevice(20)
relay_3 = OutputDevice(26)

#define the app
app = Flask(__name__)

#Define our home route
@app.route('/')
def home():
    return render_template('relay.html')

#Define the relay functions
@app.route('/relay1')
def relay1():
    relay_1.on()
    relay_2.off()
    relay_3.off()
    return render_template('relay.html')

@app.route('/relay2')
def relay2():
    relay_1.off()
    relay_2.on()
    relay_3.off()
    return render_template('relay.html')

@app.route('/relay3')
def relay3():
    relay_1.off()
    relay_2.off()
    relay_3.on()
    return render_template('relay.html')

@app.route('/off')
def off():
    relay_1.off()
    relay_2.off()
    relay_3.off()
    return render_template('relay.html')

#Run our app
if __name__ == '__main__':
    app.run(host='0.0.0.0')
