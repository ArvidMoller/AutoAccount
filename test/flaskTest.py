from flask import Flask     # type: ignore

app = Flask(__name__)

x ="jhkaerbghjleavrg"

@app.route("/")
def hello_world():
    return x