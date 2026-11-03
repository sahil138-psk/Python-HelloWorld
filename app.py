
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        s = request.form["symptom"].lower()

        if s == "fever":
            result = "General Medicine"
        elif s == "tooth pain":
            result = "Dental Department"
        elif s == "eye problem":
            result = "Eye Department"
        elif s == "skin problem":
            result = "Dermatology"
        else:
            result = "No rule found"

    return render_template("index.html", result=result)

app.run()
