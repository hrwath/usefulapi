from flask import Flask

app = Flask(__name__)

@app.route("/even/<int:number>")
def even(number):
    return {
        "even": not(number & 1)
    }