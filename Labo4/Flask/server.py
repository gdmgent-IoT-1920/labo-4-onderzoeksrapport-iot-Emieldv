#import librabies
from flask import Flask, render_template, request
from sense_hat import SenseHat
from PIL import ImageColor

#sensehat instantiëren
sense = SenseHat()

#flask server instantiëren
app = Flask(__name__)

sense_values = {
    "value": "#000000",
    "type": "hex",
    "message": ""
}

@app.route("/")
def index():
    return "hello world"

@app.route("/hello")
def hello():
    return "you have reached the pi of E-De-Vleeschouwer"

@app.route("/sensehat", methods = ["GET", "POST"])
def color():
    if(request.method == "POST"):
        sense_values["value"] = request.form["senseColor"]
        sense_values["message"] = request.form["message"]
        rgbcolor= ImageColor.getrgb(sense_values["value"])
        sense.show_message(sense_values['message'], text_colour=rgbcolor)
        # sense.clear(ImageColor.getrgb(sense_values["value"]))
    return render_template("sensehat.html.j2", sense_values = sense_values)

#server constants
host  = "192.168.0.103"
port = 8080
if __name__ == "__main__":
    app.run(host = host, port = port, debug=True)