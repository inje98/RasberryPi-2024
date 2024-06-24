from flask import Flask, render_template_string
import RPi.GPIO as GPIO
import time

ledR = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledR, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string('''
        <h1>LED Control</h1>
        <button onclick="location.href='/led/on'" style="padding: 10px 20px; font-size: 16px;">Turn LED ON</button>
        <button onclick="location.href='/led/off'" style="padding: 10px 20px; font-size: 16px;">Turn LED OFF</button>
    ''')

@app.route("/led/on")
def on():
    GPIO.output(ledR, False)
    return render_template_string('''
        <h1>LED is now ON</h1>
        <button onclick="location.href='/'" style="padding: 10px 20px; font-size: 16px;">Go Back</button>
    ''')

@app.route("/led/off")
def off():
    GPIO.output(ledR, True)
    return render_template_string('''
        <h1>LED is now OFF</h1>
        <button onclick="location.href='/'" style="padding: 10px 20px; font-size: 16px;">Go Back</button>
    ''')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10111, debug=True)
