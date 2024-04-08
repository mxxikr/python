# 입력과 출력 생각

# result = GuGu(2) 
# GuGu 함수에 2 입력값 주면 변수에 결괏값 대입

#연속된 자료형은 리스트 자료형 형태

def GuGu(n):
    result = [] #결괏값을 담을 리스트 생성
    result.append(n*1)
    result.append(n*2)
    result.append(n*3)
    result.append(n*4) 
    result.append(n*5)
    result.append(n*6)
    result.append(n*7)
    result.append(n*8)
    result.append(n*9) # 반복문이 너무 많음
    return result

print(GuGu(2))

# 테스트
i = 1
while i < 10:
    print(i)
    i = i + 1

# 실제 적용
def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i += 1
    return result

print(gugu(2))

# 구체적으로 단계적으로 접근!
