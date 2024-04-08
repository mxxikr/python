import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser') # parser의 종류는 html -> indeed_result 변수에서 가져온 html을 이용해 html 정보를 텍스트로 추출
pagination = indeed_soup.find("div", {"class" : "pagination"} ) # 추출한 정보에서 "div" 태그와 pagination class를 가진 정보를 추출
# indeed_soup의 find를 사용해 찾은 결과를 pagination 변수에 대입
                                        # 이름, attribute
links = pagination.find_all('a') # 추출한 정보에서 'a' 태그 모두 추출, 모든 링크의 리스트 반환
# pagination 변수에서 리스트를 생성해 pages 변수에 대입
pages = [] # 빈 리스트 생성
for link in links[:-1]: # pages에 있는 각 page마다 찾은 span 정보를 spans 리스트에 대입
    pages.append(int(link.string)) # string으로 페이지 숫자 가져옴 -> int 사용해 정수로 변경해야함
max_page = pages[-1] # 가장 마지막 페이지 숫자를 변수에 지정

for n in range(max_page): # range 함수 : 넣은 값 크기만큼 배열 생성
    print(f"start={n*50}")
# 페이지를 계속해서 request 하는 방법

