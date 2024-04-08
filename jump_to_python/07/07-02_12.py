# 컴파일 옵션
    # DOTALL(S) : .이 줄바꿈 문자를 포함하여 모든 문자와 매치 가능하게 함
    # IGNORECASE(I) : 대소문자에 관계없이 매치 가능하게 함
    # MULTILINE(M) : 여러줄과 매치가능하게 함(^, $관련)
    # VERBOSE(X) : verbose 모드를 사용할 수 있게 함(정규식 보기 편하게, 주석 사용가능)
# 약어 사용 가능 : re.VERBOSE -> re.X

# re.VERBOSE : 이해하기 어려운 정규식을 주석 또는 줄 단위로 구분 가능하게 하는 옵션
# 문자열에 사용된 whitespace는 컴파일 할때 삭제됨([] 안에 사용된 whitespace 제외)

import re

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

print(charref)

charref = re.compile(r"""
&[#]    # Start of a numeric entity reference
(
    0[0-7]+ # Octal form
    |[0-9]+ # Decimal form
    |x[0-9a-fA-F]+ # Decimal form
    )
    ; # Trailing semicolon
""", re.VERBOSE) 

print(charref)