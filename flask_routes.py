from flask import Flask
import datetime

app = Flask(__name__)

data = datetime.datetime.now()

message = "Bom dia!"

if data.hour >= 12 and data.hour < 18:
    message= "Boa tarde!"

if data.hour >= 18 and data.hour < 23:
    message= "Boa noite!"

data = data.strftime("%d/%m/%Y %H:%M:%S %p")

@app.route("/")
def home():
    return {"data": "Home Page"}

@app.route("/current_datetime")
def current_datetime():

    return {
        "current_datetime": data,
        "message": message
    }