# isinstance(object, class): 첫번째 인수로 인스턴스, 두번째 인수로 클래스이름
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지 판단하여 참이면 True, 거짓이면 False
class Person: pass

a = Person()
b = a
c = 3
d = isinstance(a, Person)
print(d)
d = isinstance(b, Person)
print(d)
d = isinstance(c, Person)
print(d)
