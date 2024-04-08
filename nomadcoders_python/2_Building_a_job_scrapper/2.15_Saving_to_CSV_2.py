import csv # 파이썬에서 제공하는 csv를 다루는 패키지

def save_to_file(jobs):
    file = open("jobs.csv", mode="w", newline='', encoding="utf-8") # 파이썬에서 제공하는 함수, 파일 여는 기능 -> 파일이 없으면 생성 # csv파일 쓰기모드로 오픈 # newline=''데이터 띄어쓰기 없이 들어가는 옵션
    writer = csv.writer(file) # 파일 객체를 csv.writer에 넣음 
    writer.writerow(["title", "company", "location", "link"]) # writerow 메서드를 통해 list 데이터 추가
    for job in jobs:
        writer.writerow(list(job.values())) #딕셔너리의 값만 가져옴 -> type이 dict_values이기 때문에 list로 변환
    return
