# 전방 탐색(Lookahead Assertions) 확장 구문 : 정규식 안에 이 확장 구문 사용 시 암호문처럼 알아보기 어렵게 바뀜
    # 긍정(positive)형 전방 탐색(?=...) : ...에 해당되는 정규식과 매치 , 조건이 통과되어도 문자열 소비X
    # 부정(negative)형 전방 탐색(?!...) : ...에 해당되는 정규식과 매치 X, 조건이 통과 되어도 문자열 소비X

import re

p = re.compile(".+:")
# . : \n을 제외한 모든 문자와 매치
# + : 앞에 문자 1번 이상 반복 (3회 반복)
m = p.search("http://google.com")
print(m.group())

## 긍정형 전방탐색

p = re.compile(".+(?=:)") # 정규식 : 부분에 긍정형 전방탐색기법 적용
# 기존 정규식과 검색에서는 동일한 효과
# : 에 해당하는 문자열이 정규식 엔진에 의해 소비 X -> 검색 결과에서 : 제거 후 반환
# (검색에는 포함되지만 검색 결과에는 제외)
m = p.search("http://google.com")
print(m.group())

# .*[.].*$ : 파일이름 + . + 확장자 정규식
    # . : \n 제외하고 모든 문자 매치
    # * : 0번 이상 반복
    # "." 문자와 매치
    # . : \n 제외하고 모든 문자 매치
    # * : 0번 이상 반복
    #  $ : 문자열 끝 매치

# .*[.][b^].*$ : 확장자가 bat인 파일 제외하는 정규식
    # 확장자가 b로 시작하면 X
    # 확장자 bar도 걸러냄

# .*[.]([^b]..|.[^a].|..[^t])$ : 확장자가 bat인 파일 제외하는 정규식
    # 첫번째 문자가 b가 아니거나, 두번째 문자가 a가 아니거나, 세번째 문자가 t가 아닌 경우
    # 확장자 문자 개수 2개인 케이스는 포함하지 않음

# .*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$ : 확장자의 문자 개수가 2개여도 통과되는 정규식

## 부정형 전방탐색
# .*[.](?!bat$).*$ : 확장자가 bat이 아닌 경우에만 통과
    # bat 문자열이 있는지 조사하는 과정에서 문자열 소비X -> bat이 아니라고 판단되면 정규식 매치 진행
# .*[.](?!bat$|exe$).*$ : 확장자 bat,exe가 아닌 경우