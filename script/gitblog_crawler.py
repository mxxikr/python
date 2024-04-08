from bs4 import BeautifulSoup as bs
import requests
import time

mxxikr_source = "https://mxxikr.github.io/"
minjee_source = "https://jmj3047.github.io/"
source = mxxikr_source

def get_post_mxxikr(source):
    post_list = []
    response = requests.get(source)
    html = response.text
    soup = bs(html, 'html.parser')      

    for i in soup.select('li.page-index > span.text-muted'):
        page = i.get_text()
        page_range = int(page.split("/")[1].strip())
    
    for n in range(1,page_range+1):
        if n == 1:
            response = requests.get(source)
        else:
            response = requests.get(source + f"page{n}/")

        if response.status_code == 200:
            html = response.text
            soup = bs(html, 'html.parser')                    
                
            title = soup.select('div.post-preview > h1 > a')
            
            for i in title:
                post_list.append(i.get_text())

        else : 
            print(response.status_code)
    return post_list

def diff_list(source):
    before = get_post_mxxikr(source)
    time.sleep(10) # 2일 후
    latest = get_post_mxxikr(source)

    return list(set(before) - set(latest))

if __name__ == '__main__':
    while True: 
        diff_list(mxxikr_source)
