# 입력 값 : 1부터 999
# 출력 값 : 3의 배수와 5의 배수의 총합

# 1000 미만의 자연수 구하는 방법

n = 1
while n < 1000:
    print(n)
    n += 1

for n in range(1, 1000):
    print(n)

# 3과 5의 배수 구하는 방법
for n in range(1, 1000):
    if n % 3 == 0:
        print(n)

#최종 풀이

result = 0
n = 1

for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0: # 3의 배수와 5의 배수되는 값 이중으로 더해지지 않기 위해 OR 연산자 사용
        result += n

print(result)
