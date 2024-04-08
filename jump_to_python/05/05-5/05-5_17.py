# map(f, iterable) : 함수(f)와 반복 가능한 자료형을 입력으로 받아 
# 각 요소를 함수 f가 수행한 결과로 묶어서 돌려줌

#1
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

#2
def two__times(x):
    return x*2

a = map(two__times, [1, 2, 3, 4])
a = list(a)
print(a)

#3
a = map(lambda x: x*2, [1, 2, 3, 4])
a = list(a)
print(a)