a = 1 # 변수에 숫자 대입
b = 2
print(a + b) # 출력

a = "Python" # 변수에 문자 대입
print(a) # 출력


## 조건문 if
a = 3
if a > 1: # a가 1보다 클 경우
    print("a is greater than 1") # 문장 출력


## 반복문 for
for a in [1, 2, 4]: # [1, 2, 4]리스트 앞에서부터 하나씩 꺼내서 a에 대입
	print(a) #print(a)를 수행


## 반복분 while
i = 0
while i < 3: # i값이 3보다 작은 동안
    i = i + 1 # i값에 1 추가
    print(i) # 출력


## 함수

def add(a, b):
    return a + b

result = add(45, 33)
print(result)