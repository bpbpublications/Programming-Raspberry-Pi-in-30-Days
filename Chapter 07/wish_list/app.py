# import libraries
from flask import Flask, request, g, render_template, session
import sqlite3
import random
#Define the app here
#This is needed so Flask knows where all files are stored
app = Flask(__name__)
# Change this session key to whatever want to use as long as it's secure
app.secret_key = "4534lgffdjg_8ohldfhs"

#Define the route 
#In this case this is the root route
@app.route("/", methods=["POST", "GET"])
#This function renders the HTML template
def home():
    # Add a session to the wish list and the all the items
    session["all_items"], session["wish_list"] = get_db()
    return render_template("index.html", all_items=session["all_items"], wish_list=session["wish_list"])

#Add this function to add our form and add POST to our method
@app.route('/addmodel', methods=["POST"])
def addmodel():
    # Append a new model
    session["wish_list"].append(request.form["select_items"])
    # add this to modify the sessions
    session.modified = True
    # Return the same template as with the home route
    return render_template("index.html", all_items=session["all_items"], wish_list=session["wish_list"])

# Add this function to remove a model
@app.route('/removemodel', methods=["POST"])    
def removemodel():
    # Reference the checkboxes in the form
    checked_boxes = request.form.getlist("check")
    # add a for loop and conditional to ensure that the item is removed
    # pop is used to remove an entry from a list 
    for item in checked_boxes:
        if item in session["wish_list"]:
            index_model = session["wish_list"].index(item)
            # Remove board model here
            session["wish_list"].pop(index_model)
            # Refresh session here
            session.modified = True
    return render_template("index.html", all_items=session["all_items"], wish_list=session["wish_list"])



#Get the database with this function
def get_db():
    # This returns the value of the named attribute in this case the database
    db = getattr(g, '_database', None)
    # If the database is none it connects to our database
    if db is None:
        db = g._database = sqlite3.connect('raspberrypi.db')
        # Here we create a cursor to execute commands
        cur = db.cursor()
        # Here we select name from models
        cur.execute("SELECT * from models")
        # Here we query all data
        all_data = cur.fetchall()
        # Convert data to string
        all_data = [str(val[0]) for val in all_data]
        # add our wish list here copy is used to copy our data
        wish_list = all_data.copy()
        # We will use random to randomize our wish list
        random.shuffle(wish_list)
        # We will slice our main model data to only have five
        wish_list = wish_list[:5]
    # Here we fetch our data as a tuple
    return all_data, wish_list

# This is the teardown function
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    # If the database is not none we close the database
    if db is not None:
        db.close()


#This is used to run the code directly
# Change the host to 0.0.0.0 to make it available to all hosts
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)