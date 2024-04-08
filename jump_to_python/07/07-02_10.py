# 컴파일 옵션
    # DOTALL(S) : .이 줄바꿈 문자를 포함하여 모든 문자와 매치 가능하게 함
    # IGNORECASE(I) : 대소문자에 관계없이 매치 가능하게 함
    # MULTILINE(M) : 여러줄과 매치가능하게 함(^, $관련)
    # VERBOSE(X) : verbose 모드를 사용할 수 있게 함(정규식 보기 편하게, 주석 사용가능)
# 약어 사용 가능 : re.IGNORECASE -> re.I

# re.IGNORECASE : 대소문자 구별없이 매치 수행할때 사용하는 옵션

import re

p = re.compile('[a-z]+', re.IGNORECASE)
a = p.match('python')
print(a)

p = re.compile('[a-z]+', re.IGNORECASE)
a = p.match('Python')
print(a)

p = re.compile('[a-z]+', re.IGNORECASE) # [a-z] 정규식은 소문자만 의미하지만 옵션으로 대소문자 구별 X
a = p.match('PYTHON')
print(a)
