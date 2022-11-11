from Flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Use flask to set up SQL connection

# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///registration.db'
# DB = SQLAlchemy(app) 

#---------------------------------------------
#Main Page

# @app.route("/")
# def home():
#    return render_template('home.html')
# if __name__ == '__main__':
#    app.run()

#---------------------------------------------
#User Inputs their information

@app.route("/")
def home():
   return render_template('../predictor.html')

#---------------------------------------------
#prediction after processing input data
    
# @app.route("/prediction")
# def input():

#     return 

#---------------------------------------------

if __name__ == "__main__":
    app.run()