# webbrowser : 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈

import webbrowser # 웹 브라우저를 자동으로 실행
webbrowser.open("http://google.com") # 해당 URL인 google.com으로 접속
# webbrowser.open() : 웹브라우저가 이미 실행된 상태일경우 입력주소로 이동, 실행 X시 새로 웹브라우저를 실행한 후 해당 주소로 이동
webbrowser.open_new("http://google.com")
# webbrowser.open_new() : 웹브라우저가 실행된 상태이더라도 새로운 창으로 해당주소가 열림