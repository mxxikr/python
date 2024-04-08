import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages(): # 최대 페이지 구하는 함수
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class" : "pagination"} ) 

    links = pagination.find_all('a')

    pages = [] 
    for link in links[:-1]:
            pages.append(int(link.string)) 
    max_page = pages[-1] 
    return max_page

def extract_jobs(html_result): # job title과 company 이름 추출하는 함수
    title = html_result.find("h2", {"class":"title"}).find("a")["title"] # 첫번째 찾은 결과를 보여줌
    company = html_result.find("span", {"class" : "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = (str(company_anchor.string))
    else:
        company = (str(company.string))
    company = company.strip() # whitespace를 없애줌
    location = html_result.find("div", {"class" : "recJobLoc"})['data-rc-loc'] # div안에 있는 attribute에 접근
    job_id = html_result["data-jk"]
    return {
    'title': title, 
    'company' : company, 
    'location' : location, 
    "link" : f"https://www.indeed.com/viewjob?jk={job_id}"
    }

def extract_indeed_jobs(last_page): # 마지막 페이지까지 job정보 추출하는 함수
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"}) # soup의 html 리스트 전부를 가져옴
        for result in results:
            job = extract_jobs(result) #result가 html을 담고 있음
            jobs.append(job)
    return jobs