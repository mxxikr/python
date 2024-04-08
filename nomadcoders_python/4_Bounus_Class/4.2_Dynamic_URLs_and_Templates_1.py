from flask import Flask
app = Flask("SuperApp") #앱을 만들기 위한 코드 ""안에 앱이름 대입

@app.route("/") # @(데코레이터) : "/"에 접속요청시 바로 아래 있는 실행할 함수를 찾음
def home():
    return "Hello! Welcome to mi casa!"

#dynamic urls
@app.route("/<username>") # <> placeholder : flask가 potato함수를 username 인자와 함께 호출
def potato(username): # potato함수에 username 매개변수가 있어야 작동
    return f"Hello {username} how are you doing"

app.run() # localhost에 서버를 구축해 웹사이트로 이동할 수 있음
# /는 웹사이트 url을 의미함 -> /로 접속 요청을 해 파이썬 함수를 실행