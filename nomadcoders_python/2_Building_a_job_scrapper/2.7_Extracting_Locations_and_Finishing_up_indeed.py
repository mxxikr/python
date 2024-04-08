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
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"}) # find_all : soup의 html 리스트 전부를 가져옴
    for result in results:
        title = result.find("h2", {"class":"title"}).find("a")["title"] # find : 첫번째 찾은 결과를 보여줌
        company = result.find("span", {"class" : "company"}) 
        company_anchor = company.find("a")
        if company_anchor is not None: # a태그(링크)가 있을 경우
            company = (str(company_anchor.string)) # strip()을 사용하기 위해 string type으로 변환
        else: # a태그(링크)가 없을 경우
            company = (str(company.string))
        company = company.strip() # strip() : string의 whitespace를 없애줌
        print(title, "---", company)
    return jobs