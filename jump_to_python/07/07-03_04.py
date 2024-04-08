## sub 메서드 : 정규식과 매치되는 부분을 다른 문자로 바꿀 수 있음

import re

p = re.compile('(blue|white|red)')
m = p.sub('colour', 'blue socks and red shoes')
# sub 매서드(바꿀 문자열, 대상문자열)
print(m)

# 문자열 바꾸기 횟수 제어 : sub 메서드 세번째 매개변수로 count값넘김
m = p.sub('colour', 'blue socks and red shoes', count=1)
# 처음 일치하는 blue만 colour라는 문자열로 한번 바꾸기 실행
print(m)

## subn 메서드 : sub와 동일한 기능을 하지만 반환결과를 튜플로 돌려줌
    # 돌려준 튜플의 첫번째 요소 : 변경된 문자열, 두번쨰 요소 : 바꾸기가 발생한 횟수

p = re.compile('(blue|white|red)')
m = p.subn('colour', 'blue socks and red shoes')
print(m)

p = re.compile('(blue|white|red)')
m = p.subn('colour', 'blue socks and red shoes', count=1)
print(m)

## sub 메서드 사용시 참조구문 사용
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
m = p.sub("\\g<phone> \\g<name>", "park 010-1234-1234")
# sub의 바꿀 문자열 부분에 \g<그룹이름> 사용 시 정규식 그룹이름 참조 가능
print(m)

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
m = p.sub("\\g<2> \\g<1>", "park 010-1234-1234")
# sub의 바꿀 문자열 부분에 \g<참조번호> 사용 시 정규식 그룹이름 참조 가능
print(m)

## sub 메서드의 첫번째 매개변수로 함수 넣기
def hexrepl(match): # hexrepl 함수 : match 객체를 입력으로 받아 16진수로변환하여 돌려주는 함수
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
m = p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.') # 바꿀 문자열 부분에 함수 넣기
# 대상 문자열에서 정규식에 매치되는 객체를 hexrepl 함수 대입
print(m)
# sub 첫번쨰 매개변수로 함수 사용시 정규식과 매치된 match 객체가 입력
# 매치된 문자열은 함수의 반환값으로 변환
