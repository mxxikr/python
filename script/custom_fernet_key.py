from cryptography.fernet import Fernet
import base64

key = "airflow test"
print("str key:", key )     #airflow test

#// Encode bytes using the URL and filesystem-safe Base64 alphabet
#// 인코딩 후 패딩 기호(=)를 제거
str_encoded_no_padding = base64.urlsafe_b64encode(bytes(key, 'UTF-8')).decode("UTF-8").rstrip("=") 
print('str_encoded_no_padding:', str_encoded_no_padding) 
#// str_encoded_no_padding: SEFQUFkrLz1-IUAjJCVeJio

#// Decode bytes using the URL and filesystem-safe Base64 alphabet
#// 패딩 기호(=)를 복원한 후 디코딩합니다
str_encoded = str_encoded_no_padding + ("=" * (4 - (len(str_encoded_no_padding) % 4)))
str_decoded = base64.urlsafe_b64decode(bytes(str_encoded, 'UTF-8')).decode("UTF-8") 
print('str_decoded:', str_decoded) 
#// str_decoded: HAPPY+/=~!@#$%^&*

print(key == str_decoded)    #// True
