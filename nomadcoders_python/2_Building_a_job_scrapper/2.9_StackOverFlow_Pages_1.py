# 1. 페이지 가져오기
# 2. request 만들기
# 3. job 추출

import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python"

stackoverflow_result = requests.get(URL)
print(stackoverflow_result) # 200값 반환 -> Okay
print(stackoverflow_result.text) # html을 text로 출력
