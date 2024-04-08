# int(x) : 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수, 정수를 입력받으면 그대로 출력
# int(x, radix) : radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려줌

a = int('3')
print(a)

a = int(3.5)
print(a)

a = int('0xea', 16)
print(a)

a = int('111', 2)
print(a)

a = hex(234)
print(a)