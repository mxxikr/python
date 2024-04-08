# all(x) : 반복가능한 자료형 x를 입력 인수로 받음 x요소중 모두 참이면 True, 거짓이 하나라도 있으면 False

a = all([1, 2, 3, 0])
print(a)

a = all([0])
print(a)

a = all([1, 3, 4, 10])
print(a)

a = all([]) # 입력인수가 빈값인 경우에는 True
print(a)