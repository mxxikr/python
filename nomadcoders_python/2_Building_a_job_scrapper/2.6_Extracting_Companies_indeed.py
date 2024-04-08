import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class" : "pagination"} ) 

    links = pagination.find_all('a')

    pages = [] 
    for link in links[:-1]:
            pages.append(int(link.string)) 
    max_page = pages[-1] 
    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"}) # soup의 html 리스트에서 직업관련 내용 태그 찾음
    for result in results: # jobsearch-SerpJobCard 리스트 하나씩 확인(result = 각 일자리)
        title = result.find("h2", {"class":"title"}).find("a")["title"] # 하위태그가 겹겹이 있을 경우 string 사용 시 None값 반환
        print(title) # result를 이용해서 일자리 이름 출력
    return jobs