import requests, json
import pandas as pd
import json

csv_path = 'C://Users//mxxikr/Downloads//편의점_좌표.csv'
rest_api_key = "1d419155a29507b8c07d9fee97dbb154"

def get_location(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    headers = {"Authorization": "KakaoAK {}".format(rest_api_key)}
    api_json = json.loads(requests.get(url, headers=headers).text)
    return api_json

def extract_path_to_csv(csv_path):
    df = pd.read_csv(csv_path, encoding='utf-8')
    extract_address = df['address'].str.extract(r'\](.*)', expand=False).str.strip()

    return extract_address

def result_location(addr):
    api_json = get_location(addr)

    if api_json['documents']:
        address = api_json['documents'][0]['address']
        x = address['x']
        y = address['y']
        return x, y
    else:
        return None, None

def main():
    extract_address = extract_path_to_csv(csv_path)

    x_list, y_list, address = [], [], []
    for i in range(len(extract_address)):
        x, y = result_location(extract_address[i])
        x_list.append(x)
        y_list.append(y)
        address.append(extract_address[i])

    df = pd.DataFrame({'address' : address, 'x': x_list, 'y': y_list})
    df.to_csv('address_convert_xy.csv', encoding='utf-8-sig', index=False)

if __name__ == "__main__":
    main()
