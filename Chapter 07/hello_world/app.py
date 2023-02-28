# import libraries
from flask import Flask 

#Define the app here
#This is needed so Flask knows where all files are stored
app = Flask(__name__)

#Define the route 
#In this case this is the root route
@app.route("/")
#This function returns hello world displayed in the browser
def hello():
    return "Hello World"

#Add this extra route to learn about multiple routes
@app.route("/goodbye")
def goodbye():
    return "Goodbye"

#This is used to run the code directly
# Change the host to 0.0.0.0 to make it available to all hosts
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

