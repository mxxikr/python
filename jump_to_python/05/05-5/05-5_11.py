# id(object) : 객체를 입력받아 객체의 고유 주소값(레퍼런스)를 돌려주는 함수

a = id(3)
b = 3
c = a

print(a)
print(id(b))
print(c)
print(id(3))
print(id(4))