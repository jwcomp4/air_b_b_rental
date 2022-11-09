from Flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Use flask to set up SQL connection
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///registration.db'
DB = SQLAlchemy(app) 

#---------------------------------------------
#Main Page

@app.route("/")
def homepage():

    return

#---------------------------------------------
#User Inputs their information

@app.route("/Airbnb_input")
def input():

    return 

#---------------------------------------------
#prediction after processing input data
    
@app.route("/prediction")
def input():

    return 

#---------------------------------------------

if __name__ == "__main__":
    app.run()