from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

# <type:varName>
@app.route("/<string:name1>/<string:name2>")
@app.route("/<string:name1>")
def hello(name1, name2="Josh"):
    name1 = name1.capitalize()
    name2 = name2.capitalize()
    return f"Hello, {name1}, {name2}!"