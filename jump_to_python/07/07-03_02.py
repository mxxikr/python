# 그루핑(Grouping) : 문자열이 계속해서 반복되는지 조사하는 정규식
    # ABC 문자열이 계속 반복되는지 조사 -> (ABC)+
    # ( ) : 그룹을 만들어 주는 메타 문자
        # 그룹 사용하는 이유 : 매치된 문자열 중에서 특정 부분의 문자열만 뽑기 위해
    # 그룹 중첩 사용 가능
    # 한번 그루핑한 문자열 재참조(Backreferences) 가능

import re

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group())

p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")  
# 이름 + " " + 전화번호 형태의 문자열을 찾는 정규식
# \w+ : 문자 + 숫자가 1번이상
# \s : whitespace 문자 1번 이상
# \d : 숫자 1번 이상 
# [-] : - 문자 매치
# \d : 숫자 1번 이상 
# [-] : - 문자 매치
# \d : 숫자 1번 이상
m = p.search("park 010-1234-1234")
# (\w+)그룹 : match 객체의 group(인덱스) 매서드를 사용해 그루핑된 문자열만 뽑을 수 있음
print(m.group(1))
# group(0) : 매치된 전체 문자열
# group(1) : 첫번째 그룹에 해당되는 문자열
# group(2) : 두번째 그룹에 해당되는 문자열
# group(n) : n번째 그룹에 해당되는 문자열

p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2)) # 두번째 그룹에 해당하는 문자열 뽑기


p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)") # 그룹 중첩 사용 가능 
# 바깥 -> 안쪽으로 들어갈 수록 인덱스 증가
m = p.search("park 010-1234-1234")
print(m.group(3)) # 세번째 그룹에 해당하는 문자열 뽑기


## 그루핑된 문자열 재참조
p = re.compile(r'(\b\w+)\s+\1')
# (그룹) + " " + 그룹과 동일한 단어 매치 -> 2개의 동일한 단어를 연속으로 사용해야 매치
# \b : 단어 구분자 ,\w : 문자 + 숫자 1번이상
# \s : whitespace 1번 이상
# \1 : 재참조 메타문자, 정규식 그룹 중 첫번째 그룹
m = p.search('Paris in the the spring').group()
print(m)

## 그루핑 된 문자열에 이름 붙이기
# 정규식안에 그룹이 많아지고, 정규식이 수정되면서 그룹 추가, 삭제 되면 
# 그 그룹을 인덱스로 참조한 프로그램 모두 변경해야하는 위험 발생
    # -> 그룹을 인덱스가 아닌 이름(Name Groups)으로 참조 
    # -> 정규식은 그룹 만들떄 그룹 이름 지정 가능
        #(?P<name>\w+)\s+((\d)[-]\d+[-]\d+)
            # (\w+) -> (?P<name>\w+) : (\w+) 그룹에 name 이름 지정
            # (?...) 표현식 : 정규 표현식 확장구문 -> 가독성 하락, 강력함 상승
            # (?P<그룹명>...) : 그룹에 이름 지정

p = re.compile(r"(?P<name>\w+)\s((\d+)[-]\d+[-]\d+)")
# Raw String 문자열 자체로 인식
# (\w+) : 문자 + 숫자 1번 이상인 name 그룹 ( 첫번째 그룹 )
# \s : whitespace 1번 이상
# ((\d+)[-]\d+[-]\d+) : 숫자 1번이상 + "-" + 숫자 1번이상 + "-" + 숫자 1번이상인 그룹 ( 두번째 그룹 )
# (\d+) : 숫자 1번 이상인 그룹 ( 세번째 그룹 )
m = p.search("park 010-1234-1234")
print(m.group("name")) # name이라는 그룹이름으로 참조

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
# Raw String 문자열 자체로 인식
# (\b\w+) : 단어 구분자 + 문자 or 숫자 1번 이상인 word 그룹 ( 첫번째 그룹 )
# \s : whitespace 1번 이상
# word 그룹 재참조 (?P=그룹이름)
m = p.search('Paris in the the spring').group()
print(m)