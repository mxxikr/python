from flask import Flask
app = Flask("SuperApp") #앱을 만들기 위한 코드 ""안에 앱이름 대입

@app.route("/") # @(데코레이터) : "/"에 접속요청시 바로 아래 있는 실행할 함수를 찾음
def home():
    return "Hello! Welcome to mi casa!"

@app.route("/contact") # @때문에 "/contact"에 접속 요청시 potato함수를 실행
#a = "hello" # 바로 아래있는 함수만 보기 때문에 에러발생
def potato():
    return "Contact me!"

app.run() # localhost에 서버를 구축해 웹사이트로 이동할 수 있음
# /는 웹사이트 url을 의미함 -> /로 접속 요청을 해 파이썬 함수를 실행