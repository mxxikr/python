# zip(*iterable) : 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 내장함수
# *iterable : 반복가능한 자료형 여러개 입력가능
# index랑 data를 별도 list로 가지고 있을때 묶어주려 사용

a = list(zip([1, 2, 3], [4, 5, 6]))
print(a)

a = list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(a)

a = list(zip([1, 2, 3], [4, 9, 8]))
print(a)

a = list(zip("abc", "def"))
print(a)

Number = [1, 2, 3, 4]
Name = ['hong', 'gil', 'dong', 'nim']

Number_Name = list(zip(Number, Name))
print(Number_Name)