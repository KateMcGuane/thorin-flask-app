import os
from flask import Flask # importing flask class

# Creating an instance of this class, storing in variable "app"
app = Flask(__name__) # built-in python variable


@app.route("/") # decorator (a way of passing objects)
def index():
    return "Hello, World"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)