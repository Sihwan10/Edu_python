#import Flask
from flask import Flask, render_template

#Flask 사용 app이라는 변수로 선언
app = Flask(__name__)

#최상위 경로 "/" 어떤거로 return할거냐
@app.route('/')
def index():
    return render_template("test.html")

#이 python script 실행 시 가동될 것
if __name__=="__main__":
    #모든 연결된 네트워크에서 접근 가능한 IP(0.0.0.0)와 포트 설정
    app.run(host='0.0.0.0',port=9999)