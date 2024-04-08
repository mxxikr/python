# search(): 문자열 전체 검색하하여 정규식과 매치되는지 조사 
# -> 매치 O시 match 객체 반환(정규식의 검색결과로 돌려주는 객체) 매치 X시 None 반환
import re

p = re.compile('[a-z]+')

m = p.search("python")
print(m)

m = p.search("3 python") # 문자열 전체를 검색하기 때문에 3 이후 python 문자열과 매치
print(m)