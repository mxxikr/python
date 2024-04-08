#filter(a, b) : 첫번째 인수로 함수 이름, 두번째 인수로 그 함수에 차례로 들어갈 반복가능한 자료형

def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1, -3, 2, 0 -5, 6]))

def positive2(x):
    return x > 0
print(list(filter(positive2, [1, -3, 2, 0 -5, 6])))

print(list(filter(lambda x: x > 0, [1, -3, 2, 0 -5, 6])))