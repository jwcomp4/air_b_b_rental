from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def predictor():

   return render_template("../Website/predictor.html")

if __name__ == "__main__":
    app.run(debug=True)