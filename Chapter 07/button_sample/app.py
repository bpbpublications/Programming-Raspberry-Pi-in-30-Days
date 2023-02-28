# import libraries
from flask import Flask, render_template, request 

#Define the app here
#This is needed so Flask knows where all files are stored
app = Flask(__name__)

#Define the route 
#In this case this is the root route
@app.route("/")
#This function renders the HTML template
def hello():
    return render_template("button.html")

#This route is used for the button
@app.route("/click")
def button_click():
    print("Button clicked")
    return render_template("button.html")

#This is used to run the code directly
# Change the host to 0.0.0.0 to make it available to all hosts
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)