import csv # 파이썬에서 제공하는 csv를 다루는 패키지

def save_to_file():
    file = open("jobs.csv", mode="w") # 파이썬에서 제공하는 함수, 파일 여는 기능 -> 파일이 없으면 생성
    print(file) # file을 열 때 mode 지정 가능 ( "w" = 쓰기, "r" = 읽기 )
    return
