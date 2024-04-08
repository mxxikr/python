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
    last_page = pages[-2].get_text(strip=True) # whitespace 포함되서 출력 -> strip을 사용해 없애줌 (strip=True) 사용시 beautifulsoup이 처리
    return int(last_page) # last_page를 반환할때 string -> integer로 반환(range 사용하려면 int로 변환해야함)

def extract_job(div_job):
    title = div_job.find("h2",{"class" : "mb4"}).find("a")["title"]
    company_row = div_job.find("h3").find_all("span", recursive=False) # 전부 가져오는 것 방지 -> 첫번째 단계의 span만 가져올 수 있음
    company = company_row[0]
    location = company_row[1] # 리스트의 첫번째 요소가 company, 두번째 요소가 location -> unpacking value 사용가능
    print(company.get_text(strip=True).strip("-"), location.get_text(strip=True))
    return{"title" : title}


def extract_jobs(last_page): # page를 계속 request
    jobs = [] # for 문 밖에 만들어야함
    for page in range(last_page): 
        result = requests.get(f"{URL}&pg={page + 1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs