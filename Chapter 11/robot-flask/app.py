# import libraries
from flask import Flask, render_template, request
from gpiozero import OutputDevice, PWMOutputDevice

# Define our robot and the PWM output pins
en_1 = PWMOutputDevice(12, pin_factory=factory)
en_2 = PWMOutputDevice(26, pin_factory=factory)
motor_in1 = OutputDevice(13,  pin_factory = factory)
motor_in2 = OutputDevice(21,  pin_factory = factory)
motor_in3 = OutputDevice(17,  pin_factory = factory)
motor_in4 = OutputDevice(27,  pin_factory = factory)

#Define our app
app = Flask(__name__)

#Define the Home route
@app.route('/')
def home():
    return render_template('robot.html')

#Define our functions for movement
@app.route('/forward')
def forward():
    motor_in1.on()
    motor_in2.off()
    motor_in3.on()
    motor_in4.off()
    return render_template('robot.html')

@app.route('/backward')
def backward():
    motor_in1.off()
    motor_in2.on()
    motor_in3.off()
    motor_in4.on()
    return render_template('robot.html')

@app.route('/left')
def left():
    motor_in1.off()
    motor_in2.on()
    motor_in3.on()
    motor_in4.off()
    return render_template('robot.html')

@app.route('/right')
def right():
    motor_in1.on()
    motor_in2.off()
    motor_in3.off()
    motor_in4.on()
    return render_template('robot.html')

@app.route('/stop')
def stop():
    motor_in1.off()
    motor_in2.off()
    motor_in3.off()
    motor_in4.off()
    return render_template('robot.html')

@app.route('/motorpwm', methods=['POST'])
def motorpwm():
    slider = request.form["speed"]
    slider2 = request.form["speed2"]
    en_1.value = int(slider) / 10
    en_2.value = int(slider2) / 10
    return render_template('robot.html')

#Run the app 
if __name__ == '__main__':
    app.run(host='0.0.0.0')