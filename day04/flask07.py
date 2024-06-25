# 동일한 폴더 위치에 templates 폴더를 만들고 거기에 html파일을 저장한다

from flask import Flask, request, render_template
from gpiozero import LED

app = Flask(__name__)

ledR = LED(21)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data', methods = ['POST'])
def data():
    data = request.form['led']

    if(data == 'on'):
        ledR.on()
        return home()

    elif(data == 'off'):
        ledR.off()
        return home()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 10011, debug=True)
