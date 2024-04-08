import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages(): # indeed의 페이지를 계속 추출하는 함수
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser') # parser의 종류는 html -> indeed_result 변수에서 가져온 html을 이용해 html 정보를 텍스트로 추출
    pagination = soup.find("div", {"class" : "pagination"} ) # 추출한 정보에서 "div" 태그와 pagination class를 가진 정보를 추출

    links = pagination.find_all('a') # 추출한 정보에서 'a' 태그 모두 추출, 모든 링크의 리스트 반환
# pagination 변수에서 리스트를 생성해 pages 변수에 대입
    pages = [] # 빈 리스트 생성 
    for link in links: # pages에 있는 각 page마다 찾은 span 정보를 spans 리스트에 대입
        try:
            pages.append(int(link.string)) # string으로 페이지 숫자 가져옴 -> int 사용해 정수로 변경해야함
        except TypeError as e:
            continue
        except Exception as e:
            print(f"Error! {e}")
            continue
    max_page = pages[-1] # 가장 마지막 페이지 숫자를 변수에 지정
    return max_page

def extract_indeed_jobs(last_indeed_page):
    for page in range(last_indeed_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        print(result.status_code)