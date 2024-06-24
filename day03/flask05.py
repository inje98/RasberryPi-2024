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

@app.route("/led/<state>")
def led(state):
	if state == "on":
		GPIO.output(ledR, False)
		return "<h1>LED ON</h1>"
	elif state == "off":
		GPIO.output(ledR, True)
		return "<h1>LED OFF</h1>"
	elif state == "clear":
		GPIO.cleanup()
		return "GPIO Cleanup()"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=10111, debug=True)


