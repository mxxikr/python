# match(): 문자열의 처음부터 정규식과 매치되는지 조사 
# -> 매치 O시 match 객체 반환(정규식의 검색결과로 돌려주는 객체) 매치 X시 None 반환

import re
p = re.compile('[a-z]+') # 모든 알파벳 소문자 1번이상 반복

m = p.match("python") # "python" 문자열은 정규식에 부합되므로 match 객체 반환
print(m)

m = p.match("3 python") # 처음에 나오는 3이 정규식에 부합되지않으므로 None 반환
print(m)

import re
p = re.compile('[a-z]+')
m = p.match('string goes here') # match 객체 또는 None 돌려줌
if m:
    print('Match Found: ', m.group()) # 각 그룹에 해당하는 문자열 튜플 형태로 반환
else:
    print('No match')