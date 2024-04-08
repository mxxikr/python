#re : regular expression 파이썬에서 정규표현식을 지원하는 모듈 

import re
p = re.compile('ab*') # re.compile 사용으로 정규표현식 컴파일
# p : re.compile의 결과로 돌려주는 객체, 컴파일된 패턴 객체 

# 정규식을 이용한 문자열 검색

    # match(): 문자열의 처음부터 정규식과 매치되는지 조사 
        # -> 매치 O시 match 객체 반환(정규식의 검색결과로 돌려주는 객체) 매치 X시 None 반환
    # search(): 문자열 전체 검색하하여 정규식과 매치되는지 조사 
        # -> 매치 O시 match 객체 반환(정규식의 검색결과로 돌려주는 객체) 매치 X시 None 반환
    # findall(): 정규식과 매치되는 모든 문자열(substring)을 리스트로 반환
    # finditer(): 정규식과 매치되는 모든 문자열(substring)을 반복가능한 객체로 돌려줌

