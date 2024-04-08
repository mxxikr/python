# findall(): 정규식과 매치되는 모든 문자열(substring)을 리스트로 반환

import re

p = re.compile("[a-z]+")

result = p.findall("life is too short")

print(result)
#['life', 'is', 'too', 'short']