import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page(): # 마지막 페이지 구하는 함수
    result = requests.get(URL) # html을 가져옴
    soup = BeautifulSoup(result.text, 'html.parser') # 분석 용이하게 파싱
    pagination = soup.find("div", {"class" : "pagination"} ) 

    links = pagination.find_all('a')

    pages = [] 

    for link in links[:-1]:
        pages.append(int(link.string)) 
    max_page = pages[-1] 
    return max_page

def extract_job(div_jobCard):
        title = div_jobCard.find("h2", {"class":"title"}).find("a")["title"] # 첫번째 찾은 결과를 보여줌
        company = div_jobCard.find("span", {"class" : "company"}) 
        if company: # company가 있을 경우
            company_anchor = company.find("a")
            if company_anchor is not None:
                company = (str(company_anchor.string))
            else:
                company = (str(company.string))
        else: # company가 없을 경우
            company = None # company 값에 None 값 대입
        company = company.strip() # whitespace를 없애줌
        location = div_jobCard.find("div", {"class" : "recJobLoc"})["data-rc-loc"] # div로 변환한다음 -> div 안에 있는 attribute에 접근
        job_id = div_jobCard.attrs["data-jk"]
        return {
            'title': title, 
            'company': company, 
            'location' : location, 
            'link' : f"https://www.indeed.com/viewjob?jk={job_id}"
            }

def extract_pages(last_page): # last_page 매개변수를 받는 extract_indeed_jobs 함수 생성
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Indeed : Page : {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"}) # soup의 div_jobCard 리스트 전부를 가져옴
        for result in results:
            job = extract_job(result) # result가 html을 담고 있음
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_pages(last_page)
    return jobs

