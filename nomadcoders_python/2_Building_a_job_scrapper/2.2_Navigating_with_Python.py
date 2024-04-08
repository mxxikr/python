# url에 접근
# 페이지가 몇개인지 확인 -> 최대 페이지를 코드에 알려줘서 페이지 20까지 가게함
# 페이지에 하나하나 들어감


import requests # 파이썬에서 요청을 만드는 기능을 모아둠

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
# requests 객체 안의 get 함수 사용
print(indeed_result) # 200 값 반환 -> okay 의미
print(indeed_result.text) # html을 텍스트로 출력

#beautiful soup : html에서 정보 추출하기에 좋은 package