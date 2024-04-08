class FourCal:
    def setdata(self, first, second): #클래스 안에 구현된 함수(Method)
        self.first = first
        self.second = second

    # pass #아무것도 수행하지 않는 문법, 임시코드 작성시 사용

a = FourCal() # a 객체 만들기, FourCal 클래스의 인스턴스
b = FourCal() # a 객체 만들기, FourCal 클래스의 인스턴스

a.setdata(4, 2)
b.setdata(3, 7)

print(a.first)
print(b.first)
print(a.first) # class로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값 유지

print(id(a.first))
print(id(b.first))
# print(type(a)) #a의 타입 확인 -> FourCal 클래스의 객체 확인
#type 함수: python이 자체로 가지고 있는 내장함수 -> 객체 타입 출력
