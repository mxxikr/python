# random : 난수(규칙이 없는 임의의 수)를 발생시키는 모듈
import random
a = random.random() # 0.0에서 1.0사이의 실수 중에서 난수 값을 돌려주는 예
print(a)

# random.randint(n, n) : n에서 n사이의 정수 중 난수 값 발생
a = random.randint(1, 10) # 1에서 10사이의 정수 중 난수 값 돌려줌
print(a)

# len(s) :입력값 s의 길이 (요소의 전체 개수)를 돌려주는 내장 함수
# list.pop() : 리스트의 지정위치 요소를 제거
import random # random 라이브러리 사용 

def random_pop(data): # 함수명 : random_pop 매개변수 : data
    number = random.randint(0, len(data)-1) # 0부터 4 사이의 정수중 난수값 발생
    return data.pop(number) 

if __name__=="__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(data)
        print(random_pop(data))

# random.choice() : 입력으로 받은 리스트에서 무작위로 하나를 선택하여 돌려줌
import random # random 라이브러리 사용

def random_pop2(data): # 함수명 : random_pop 매개변수 : data
    number = random.choice(data) # number 변수는 data 리스트에서 무작위로 하나를 선택해서 받은 값
    data.remove(number) # data리스트에서 number 변수 삭제
    return number

if __name__=="__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(data)
        print(random_pop2(data))

# random.shuffle : 리스트 항목을 무작위로 섞고 싶을 때 사용
import random
data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(data)
