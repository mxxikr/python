# 프로그램 수행 도중 특수한 경우에만 예외처리

class MyError(Exception): #Exception : 파이썬 내장 클래스
    def __str__(self): # __str__ 메서드 : 오류메세지를 print문으로 출력할 경우에 호출되는 메서드
        return "허용되지 않은 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError() 
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)

# say_nick("천사")
# say_nick("바보")