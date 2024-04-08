# type(object) : 입력값의 자료형이 무엇인지 알려주는 함수

a = type("abc")
print(a)

a = type(["abc"])
print(a)

a = type(open("test", 'w'))
print(a)

a = type(open("test.txt", 'w'))
print(a)

# _io.TextIOWrapper 파일 자료형