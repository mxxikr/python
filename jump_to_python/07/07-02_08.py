# re 모듈 : re.compile 사용하여 컴파일된 패턴 객체를 축약 형태로 사용가능하게 함
# 한번 만든 패턴 객체를 여러번 사용할때는 re.compile방법이 편함

import re

m = re.match('[a-z]+', "3 python")
print(m)

m = re.search('[a-z]+', "3 python")
print(m.group())

m = re.findall('[a-z]+', "3 python")
print(m)

m = re.finditer('[a-z]+', "3 python")
print(m)