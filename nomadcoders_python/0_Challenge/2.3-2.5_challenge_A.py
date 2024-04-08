import os
import requests
from bs4 import BeautifulSoup

os.system("clear")


url = "https://www.iban.com/currency-codes"


countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table") # 첫번째 table 클래스를 찾음
rows = table.find_all("tr")[1:] # table클래스에서 tr태그를 모두 찾음(1번째~끝까지: head제외) 
for row in rows: # tr태그
    items = row.find_all("td") # tr태그의 td태그를 모두 찾음(country, currency, code, number)
    name = items[0].text # tr태그의 첫번째 인덱스 string만 가져옴(country)
    code =items[2].text # tr태그의 세번째 인덱스 string만 가져옴(code)
    if name and code: # country 값과 code값이 있을 경우
        if name != "No universal currency": # 해당 값이 country 값이 아닐경우
            country = { # country 딕셔너리 생성
            'name':name.capitalize(), # country 값을 첫글자는 대문자, 나머지는 소문자로 변환
            'code': code # code값
            }
            countries.append(country) #country list에 country 딕셔너리 추가


def ask():
    try: # 실행시
        choice = int(input("#: "))
        if choice > len(countries): # country 딕셔너리 리스트의 길이보다 클 경우
            print("Choose a number from the list.")
            ask()# 함수 재실행
        else:
            country = countries[choice] # 입력숫자값 인덱스 추출
            print(f"You chose {country['name']}\nThe currency code is {country['code']}")
    except ValueError: # ValueError가 나타날 경우
        print("That wasn't a number.") # 숫자가 아니라는 안내문 출력
        ask() # 함수 재실행


print("Hello! Please choose select a country by number:")
for index, country in enumerate(countries): # countries 리스트의 원소에 순서값 부여
    print(f"#{index} {country['name']}")

ask()