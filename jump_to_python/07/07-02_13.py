# 백슬래시(\)
# 매치 X : \section = [ \t\n\r\f\v]ection
# 매치 O : \\section (이스케이프 처리)

import re

p = re.compile('\\section') # 문자열 리터럴 규칙에 따라 \\ -> \로 변경되어 전달
p = re.compile('\\\\section') # 복잡
p = re.compile(r'\\section') 
# Raw String 임을 알려 줄 수 있도록 정규식 문자열 앞에r 문자 삽입
# Raw String 규칙에 의하여 \ -> \\ 와 동일한 의미 가짐
# \section 일치하는 결과 반환

m = p.search('3 \\section')
print(m)

# Raw String : 문자열을 그 자체로 인식하게 해주는 파이썬 문법