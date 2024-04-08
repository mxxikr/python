# 컴파일 옵션
    # DOTALL(S) : .이 줄바꿈 문자를 포함하여 모든 문자와 매치 가능하게 함
    # IGNORECASE(I) : 대소문자에 관계없이 매치 가능하게 함
    # MULTILINE(M) : 여러줄과 매치가능하게 함(^, $관련)
    # VERBOSE(X) : verbose 모드를 사용할 수 있게 함(정규식 보기 편하게, 주석 사용가능)
# 약어 사용 가능 : re.MULTILINE -> re.M

# re.MULTILINE : 메타 문자인 ^(처음), $(끝)를 문자열의 각 줄마다 적용해주는 옵션
# 각 라인의 처음으로 인식 시키고 싶은 옵션 ^


import re

p = re.compile("^python\\s\\w+", re.M)  
# 각 줄마다 python 이라는 문자열로 시작하고 whitespace가 뒤에오고 그 뒤에 단어가 와야함

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data)) # 정규식과 매치되는 문자열 리스트 반환