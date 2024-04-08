import os
import requests


def restart():
    answer = str(input("Do you want to start over? y/n ")).lower() # 입력값 문자열로 치환, 대소문자 변환, lower메소드는 str.lower만 가능해서 str로 변화
    if answer == "y" or answer =="n": # 첫번째 조건 : 입력값이 유효한 값일 경우
        if answer == "n": # 두번째 조건 : 입력값이 n 일 경우
            print("k. bye!")
            return
        elif answer == "y": # 두번째 조건 : 입력값이 y 일 경우
            main() # main 함수 (반복)
    else:
        print("That's not a vaild answer.")
        restart()

def main(): # 반복할 본문 함수
    os.system('clear') # clear
    print("Welcome to IsItDown.py!\nPlease write a URL or URLS you want to check. (separated by comma)")
    urls = str(input()).lower().split(",") # 입력값 대소문자 변환, "," 구분자 지정, lower메소드는 str.lower만 가능해서 str로 변화
    for url in urls:
        url = url.strip() # 입력값으로 받은 url의 whitespace값을 제거
        if "." not in url: # url에 .값이 포함되지 않을 경우 (url 형태가 아닐 경우)
            print(url, "is not a vaild URL.")
        else: # url 형태일 경우
            if "http" not in url: # http 문자열이 포함되지 않을 경우
                url = f"http://{url}" # http를 붙여줌
            try: # 예외처리
                request = requests.get(url)
                if request.status_code == 200:
                    print(url, "is up!")
                else:
                    print(url, "is down!")
            except: # 오류가 나는 모든 url은 down 알림
                print(url, "is down!")
    restart()


main()