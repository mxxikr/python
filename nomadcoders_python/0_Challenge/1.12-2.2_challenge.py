import os
import requests

ans = "y"

def answer():
    ans = input("Do you want to start over? y/n ")
    if ans == "y":
        os.system("clear")
        return ans
    elif ans == "n":
        print("k. bye!")
        return ans
    else:
        print("That's not a vaild answer.")
        answer()


while ans != "n":
    check_url = input("Welcome to IsItDown.py!\nPlease write a URL or URLS you want to check. (separated by comma)\n").split(",")
    if ".com" in check_url:
        for urls in check_url:
            if "http://" in urls:
                url = f"{urls.strip().lower()}"
            else:
                url = f"http://{urls.strip().lower()}"
            url_status = requests.get(url)
            if url_status.status_code == 200:
                print(f"{url} is up!")
            else:
                print(f"{url} is down!")
    else:
        print("url is not a vaild URL.")
    answer()

# def answer(a):
# 	Please write a URL or URLS you want to check. (separated by comma)

# input으로 url 작성 (http 유무에 관계없이 쉼표로 구분된 url 수에 대해 수용 , 공백,대문자, 소문자 유무 허용)

# if url 주소 O 일 경우 (.com .net .co.kr .org in url)
# 	if: http:// X일 경우
# 		http:// 붙임 url = [p;l,mnb .lo9i
# 	else: http:// O일 경우
# 		url = f"{url.strip().lower()}"
# 	result_url = request.get(url)
# 		if: url status_code가 200일 경우
# 			http://url is up! 
# 		else: url status_code가 200가 아닐 경우	
# 			http://url is down!
# else: url 주소 X 일 경우 (.com .net .co.kr .org not in url) else
# 	url is not a vaild URL.



# 	y 선택시 
# 		clear 사용 후 위 문장 반복
# 	n 선택시 
# 		print("k. bye!")
# 	그 외 선택시 
# 		print("That's not a vaild answer.")


# strip, split, status_code, for문 사용
# request 객체 사용