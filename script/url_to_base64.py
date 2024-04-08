import base64
import json
import requests
 
# 이미지 url base64로 수정
def url_to_base64(url):
    response = requests.get(url)
    content = response.content
    base64_data = base64.b64encode(content)
    base64_string = base64_data.decode('utf-8')
    return base64_string

file_url = 'https://d39tjlpv1kg2ny.cloudfront.net/building_image/k8s/117726/47563/2f188cd0-0a7a-11ee-b9cb-f9aab3d0c3a6/-1198965052.jpg'
base64_data = url_to_base64(file_url)
print(base64_data)