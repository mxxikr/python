# url에 접근
# 페이지가 몇개인지 확인
# 페이지에 하나하나 들어감 -> html에서 페이지 숫자 클릭


import requests # 요청을 만드는 기능을 모아둠

indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=0d414af81d2a24bc")
# requests 객체 안의 get 함수 사용
print(indeed_result) # 200 값 반환 -> okay 의미
print(indeed_result.text) # html 전부 가져옴

# beautiful soup : html에서 정보를 추출하기에 유용한 패키지
