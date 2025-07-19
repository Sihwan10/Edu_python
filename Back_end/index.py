from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/data',methods=['POST'])
def data():
    input_data = request.form.get("input_data")
    return f"<h3>입력된 데이터: {input_data}<h3>"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8888)