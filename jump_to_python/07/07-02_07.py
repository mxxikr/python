# match 객체의 메서드
    #group() : 매치된 문자열을 반환
    #start() : 매치된 문자열의 시작 위치 반환
    #end() : 매치된 문자열의 끝 위치 반환
    #span() : 매치된 문자열의(시작, 끝)에 해당하는 튜플 반환

import re

p = re.compile("[a-z]+")
m = p.match("python is")

a = m.group()
print(a)

a = m.start() # match 매서드는 항상 문자열 시작부터 조사하기 때문에 결괏값 항상 0
print(a)

a = m.end()
print(a)

a = m.span()
print(a)

import re

p = re.compile("[a-z]+")
m = p.search("3 python")

a = m.group()
print(a)

a = m.start()
print(a)

a = m.end()
print(a)

a = m.span()
print(a)