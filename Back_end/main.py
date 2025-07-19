# Import flask
from flask import Flask, render_template, request
import lotto

# Flask 웹 호출 정의
app = Flask(__name__)

@app.route('/lotto')
def lotto_index():
   return render_template('main.html')

@app.route('/lotto_data')
def get_lotto():
    numbers = lotto.lotto_number()
    return numbers

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=7777)