# URL접속을 /led/on, /led/off로 접속하면 led를 on, off하는 웹페이지를 만들어보자구요
from flask import Flask
import RPi.GPIO as GPIO
import time

ledR = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledR, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!!"

@app.route("/led/on")
def on():
	GPIO.output(ledR, False)
	return "<h1>led on</h1>"

@app.route("/led/off")
def off():
	GPIO.output(ledR, True)
	return "<h1>led off</h1>"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=10111, debug=True)

