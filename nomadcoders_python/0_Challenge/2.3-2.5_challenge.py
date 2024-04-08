import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")
table = soup.find("table")
tr_lists = table.find_all("tr")[1:]


country_code_list =[]

print("Hello! Please choose select a country by number:")

for tr_list in tr_lists:
    tr = tr_list.find_all("td")
    country_tr = tr[0].text
    code_tr = tr[2].text
    if country_tr and code_tr:
        if country_tr != "No universal currency":
            country = {
                'country' : country_tr,
                'code' : code_tr
            }
            country_code_list.append(country)

def choose_number():
    try:
        choice = int(input("#: "))
        if choice > len(country_code_list):
            print("Choose a number from the list")
            choose_number()
        else:
            country = country_code_list[choice]
            print(f"You chose {country['country']}\nThe currency code is {country['code']}")
    except:
        print("That wasn't a number")
        choose_number() 

for index, country in enumerate(country_code_list):
    print(f"#{index} {country['country']}")

choose_number()