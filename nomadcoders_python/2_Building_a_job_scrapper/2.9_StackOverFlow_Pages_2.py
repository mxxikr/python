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
    print(pages)


# def get_jobs():
#     last_page = get_last_page()
#     return []