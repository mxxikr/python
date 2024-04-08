import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")


code_url = "https://www.iban.com/currency-codes" # 국가별 통화 url
currency_url = "https://transferwise.com/gb/currency-converter/" # 환전 url


countries = []

codes_request = requests.get(code_url)
codes_soup = BeautifulSoup(codes_request.text, "html.parser")

table = codes_soup.find("table") # 첫번째 table 클래스를 찾음
rows = table.find_all("tr")[1:]  # table클래스에서 tr태그를 모두 찾음(1번째~끝까지: head제외)

for row in rows: # tr태그
    items = row.find_all("td") # tr태그의 td태그를 모두 찾음(country, currency, code, number)
    name = items[0].text # tr태그의 첫번째 인덱스 string만 가져옴(country)
    code =items[2].text # tr태그의 세번째 인덱스 string만 가져옴(code)
    if name and code: # country 값과 code값이 있을 경우
        if name != "No universal currency": # 해당 값이 country 값이 아닐경우
            country = {  # country 딕셔너리 생성
            'name':name.capitalize(), # country 값을 첫글자는 대문자, 나머지는 소문자로 변환
            'code': code # code값
            }
        countries.append(country) #country list에 country 딕셔너리 추가


def ask_country(text):
    print(text)
    try: # 실행시
        choice = int(input("#: "))
        if choice > len(countries):  # country 딕셔너리 리스트의 길이보다 클 경우
            print("Choose a number from the list.")
            return ask_country(text) # 함수 재실행
        else:
            print(f"{countries[choice]['name']}") # 입력 숫자값 인덱스에 대한 'name' 출력
            return countries[choice] # 입력숫자값 인덱스 반환
    except ValueError: # ValueError가 나타날 경우
            print("That wasn't a number.") # 숫자가 아니라는 안내문 출력
            return ask_country(text) # 함수 재실행


def ask_amount(a_country, b_country):# 바꿀 country, 바뀌어질 country 값을 매개변수로 가지는 ask_amount 함수
    try: # 실행시
        print(f"\nHow many {a_country['code']} do you want to convert to {b_country['code']}?")
        amount = int(input()) # 입력값 정수로 변환
        return amount # 입력한 값 반환
    except ValueError: # ValueError 발생시 예외처리
        print("That wasn't a number.") # 숫자가 아니라는 문장 출력
        return ask_amount(a_country, b_country) # 함수 재실행


print("Welcome to CurrencyConvert PRO 2000\n")
for index, country in enumerate(countries): # countries 리스트의 원소에 순서값 부여
    print(f"#{index} {country['name']}")

user_country = ask_country("\nWhere are you from? Choose a country by number.\n") # 문자열을 매개변수로 하는 aks_country함수 실행한 값이 user_country 변수
target_country = ask_country("\nNow choose another country.\n") # 문자열을 매개변수로 하는 aks_country함수 실행한 값이 target_country 변수


amount = ask_amount(user_country, target_country)

from_code = user_country['code'] # 바꿀 country의 code값 지정
to_code = target_country['code'] # 바뀔 country의 code값 지정

currency_request = requests.get(f"{currency_url}{from_code}-to-{to_code}-rate?amount={amount}") # 환전할때 페이지 url
currency_soup = BeautifulSoup(currency_request.text, "html.parser")
result = currency_soup.find("input", {"id":"rate"})

if result: # 환전 결과값이 있을 경우
    result = result['value'] # id=rate값인 input 태그의 value 값 
    amount = format_currency(amount, from_code, locale="ko_KR") # 입력 번호, 입력 country 통화 code, 로컬식별자
    result = format_currency(result, to_code, locale="ko_KR") # 출력 번호, 출력 country 통화 code, 로컬식별자
    print(f"{amount} is {result}")