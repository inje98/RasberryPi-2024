# 동일한 폴더 위치에 templates 폴더를 만들고 거기에 html파일을 저장한다

from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

ledR = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledR, GPIO.OUT)

@app.route('/')
def home():
    return render_template("index.html") # 같은 디렉토리 안의 index.html 파일을 string으로 return하는게 아닐까

@app.route('/data', methods = ['POST'])
def data():
    data = request.form['led']

    if(data == 'on'):
        GPIO.output(ledR, False)
        return home()

    elif(data == 'off'):
        GPIO.output(ledR, True)
        return home()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 10011, debug=True)
