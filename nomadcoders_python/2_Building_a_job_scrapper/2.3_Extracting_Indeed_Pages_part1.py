import requests # http request 라이브러리, python이 이해하는 객체 구조로 만들어 주지 못함. .text는 string객체를 반환함
from bs4 import BeautifulSoup

#http를 request로 get함
indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser') # parser의 종류는 html -> indeed_result 변수에서 가져온 html 소스(문자열객체)를 텍스트로 추출
pagination = indeed_soup.find("div", {"class" : "pagination"} ) # 추출한 정보에서 "div" 태그와 pagination class를 가진 정보를 추출
# indeed_soup의 find를 사용해 찾은 결과를 pagination 변수에 대입
                                        # 이름, attribute
links = pagination.find_all('a') # pagination의 'a' 태그 모두 추출해 리스트로 반환
# pagination 변수에서 리스트를 생성해 pages 변수에 대입
spans = [] # 빈 리스트 생성
for link in links: # pages에 있는 각 page마다 찾은 span 정보를 spans 리스트에 대입
    spans.append(link.find("span"))

print(spans[:-1]) # 모든 것을 가져오되, 마지막 것은 제외
# span 리스트의 0부터 마지막 요소까지 출력