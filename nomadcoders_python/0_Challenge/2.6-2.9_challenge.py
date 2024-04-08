# """
# Use the 'format_currency' function to format the output of the conversion
# format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
# """

# print(format_currency(5000, "KRW", locale="ko_KR"))

import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")


code_url = "https://www.iban.com/currency-codes"
currency_url = "https://transferwise.com/gb/currency-converter/"

country_code_list = []

codes_request = requests.get(code_url)
codes_soup = BeautifulSoup(codes_request.text, "html.parser")

table = codes_soup.find("table")
tr_lists = table.find_all("tr")[1:]

for tr_list in tr_lists:
    tr = tr_list.find_all("td")
    country_tr = tr[0].text
    code_tr =tr[2].text
    if country_tr and code_tr:
        if country_tr != "No universal currency":
            country = {
            'country':country_tr.capitalize(),
            'code': code_tr
            }
        country_code_list.append(country)


def choose_number(text):
    print(text)
    try:
        choice = int(input("#: "))
        if choice > len(country_code_list):
            print("Choose a number from the list.")
            return choose_number(text)
        else:
            print(f"{country_code_list[choice]['country']}")
            return country_code_list[choice]
    except ValueError:
            print("That wasn't a number.")
            return choose_number(text)


def convert_money(amount_country, convert_country):
    try:
        print(f"\nHow many {amount_country['code']} do you want to convert to {convert_country['code']}?")
        amount_money = int(input())
        return amount_money
    except ValueError:
        print("That wasn't a number.")
        return convert_money(amount_country, convert_country)


print("Welcome to CurrencyConvert PRO 2000\n")
for index, country in enumerate(country_code_list):
    print(f"#{index} {country['country']}")

amount_country = choose_number("\nWhere are you from? Choose a country by number.\n")
convert_country = choose_number("\nNow choose another country.\n")


amount_value = convert_money(amount_country, convert_country)

amount_code = amount_country['code']
convert_code = convert_country['code']

currency_request = requests.get(f"{currency_url}{amount_code}-to-{convert_code}-rate?amount={amount_value}")
currency_soup = BeautifulSoup(currency_request.text, "html.parser")
convert_value = currency_soup.find("input", {"id":"rate"})


if convert_value:
    convert_value = convert_value['value']
    amount_value = format_currency(amount_value, amount_code, locale="ko_KR")
    convert_value = format_currency(convert_value, convert_code, locale="ko_KR")
    print(f"{amount_value} is {convert_value}")