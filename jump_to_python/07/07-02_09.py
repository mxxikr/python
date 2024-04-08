# 컴파일 옵션
    # DOTALL(S) : .이 줄바꿈 문자를 포함하여 모든 문자와 매치 가능하게 함
    # IGNORECASE(I) : 대소문자에 관계없이 매치 가능하게 함
    # MULTILINE(M) : 여러줄과 매치가능하게 함(^, $관련)
    # VERBOSE(X) : verbose 모드를 사용할 수 있게 함(정규식 보기 편하게, 주석 사용가능)
# 약어 사용 가능 re.DOTALL -> re.S

# re.DOTALL : . 메타 문자 사용할 때 \n문자 포함하여 매치하고싶을 경우 사용하는 옵션

import re
p = re.compile('a.b')
m = p.match('a\nb') # \n는 . 메타 문자와 매치 X
print(m) # None

p = re.compile('a.b', re.DOTALL) #여러 줄로 이루어진 문자열에서 \n에 상관없이 검색
m = p.match('a\nb')
print(m)
print(m.group())

p = re.compile('a.b', re.S)
m = p.match('a\nb')
print(m)