# 1. 페이지 가져오기
# 2. request 만들기
# 3. job 추출

import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser') # parser의 종류는 html -> stackoverflow_result 변수에서 가져온 html 소스(문자열객체)를 텍스트로 추출
    pages = soup.find("div", {"class" : "s-pagination"}).find_all("a") # 추출한 정보에서 "div" 태그와 s-pagination class를 가진 정보를 추출
    # pages = pages[0:-1] # 마지막 next 값 빼고 출력
    # print(pages[-1]) # 가져온 숫자 중 가장 마지막 숫자 출력
    pages = pages[-2] # 마지막 next값 지우고 마지막 숫자(뒤에서 두번째) 출력
    print(pages)


# def get_jobs():
#     last_page = get_last_page()
#     return []