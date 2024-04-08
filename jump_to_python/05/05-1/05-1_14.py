class Family:
    lastname = "김" # 클래스 변수 : 클래스 안에 변수를 선언하여 생성

print(Family.lastname)

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))

Family.lastname = "박" #클래스 변수 값 변경

print(a.lastname) #클래스로 만든 객체의 lastname값도 모두 변경됨 
print(b.lastname) #클래스의 변수는 클래스로 만든 모든 객체에 공유됨

print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))
