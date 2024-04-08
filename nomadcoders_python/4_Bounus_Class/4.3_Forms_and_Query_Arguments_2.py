from flask import Flask, render_template, request
# render_template를 import하면 html을 메인으로 불러올 수 있음
# 사용자가 입력한 단어를 추출하기 위해 request import
app = Flask("SuperApp") #앱을 만들기 위한 코드 ""안에 앱이름 대입

@app.route("/") # @(데코레이터) : "/"에 접속요청시 바로 아래 있는 실행할 함수를 찾음
def home():
    return render_template("potato.html") # frontend에 해당하는 파일이 .py가 아닌 .html에서 읽어올 수 있게 함
# render_template 함수를 보고 flask가 templates폴더에서 html파일을 찾음

@app.route("/report")
def report(): # 인자가 없음 -> 사용자가 찾으려고 하는 단어를 가져오고 싶을때
    word = request.arg.get('word')
    return render_template("report.html", searchingBy = word, potato="sexy") # data를 넘겨주는 방법
# flask가 html을 쭉보고 있다가 변수를 발견하면 html의 {{}}에 변수를 대입하여 사용자에게 보여줌 -> rendering

app.run() # localhost에 서버를 구축해 웹사이트로 이동할 수 있음
# /는 웹사이트 url을 의미함 -> /로 접속 요청을 해 파이썬 함수를 실행