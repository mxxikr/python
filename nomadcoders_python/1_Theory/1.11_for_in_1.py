# for : 순차적으로 하나씩 작업 가능
# 데이터를 순서대로 처리할 때 사용
# string, tuple, list 같은 배열의 요소를 순차적으로 가리킴

days = ("Mon", "Tue", "Wed", "Thu", "Fri")

#days = 배열이름
for day in days: # day :변수이름, 초기값 설정 X, 작업할때 값 대입 
    if day == "Wed": # day 변수는 for문이 실행될 때 생성(선언)
        break # for문 끝내기
    else:
        print(day)

for day in [1, 2, 3, 4, 5, 6, 7]:
    print(day)


for letter in "nicolas": # 문자열도 배열이기 때문에 순차적으로 출력할 수 있음
    print(letter)
