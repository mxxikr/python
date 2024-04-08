# any(x) : 반복가능한 자료형 x를 입력 인수로 받음 x요소중 하나라도 참이면 True, 모두 거짓이면 False

a = any([1, 2, 3, 0])
print(a)

a = any([1, 3, 4, 10])
print(a)

a = any([0])
print(a)

a = any([""])
print(a)

a = any([0, ""])
print(a)


a = any([]) # 입력인수가 빈값인 경우에는 False
print(a)