# 문자열 소비가 없는 메타 문자

# | 메타 문자 : or과 동일한 의미
    # A | B : A 또는 B

import re

p = re.compile('Crow|Servo')  #Crow 또는 Servo
m = p.match('CrowHello')
print(m)

# ^ 메타 문자 : 문자열의 맨 처음과 일치함을 의미 
    # re.MULTILINE 컴파일 옵션 사용할 경우 : 여러줄 문자열일 때 각 줄의 처음과 일치
    # 메타 문자가 아닌 문자 자체로 매치하고 싶은 경우에는 \^사용
m = re.search('^Life', 'Life is too short')
print(m)
m = re.search('^Life', 'My Life')
print(m)

# $ 메타 문자 : ^ 메타 문자와 반대 경우, 문자열 끝과 매치
    # 메타 문자가 아닌 문자 자체로 매치하고 싶은 경우에는 \$사용
print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))
# 검색할 문자열이 short로 끝난 경우에만 매치

# \A 메타문자 : 문자열의 처음과 매치 = ^ 메타문자 의미
# re.MULTILINE 옵션 사용 시 ^ 메타문자와 다르게 전체 문자열의 처음만과= 매치
m = re.search('\\ALife', 'Life is too short')
print(m)
m = re.search('\\ALife', 'My Life')
print(m)

# \Z 메타문자 : 문자열의 끝과 매치 = $ 메타문자 의미
# re.MULTILINE 옵션 사용 시 $ 메타문자와 다르게 전체 문자열의 끝과 매치
print(re.search('short\\Z', 'Life is too short'))
print(re.search('short\\Z', 'Life is too short, you need python'))

# \b 메타문자 : 단어구분자(word boundary), 보통 단어는 whitespace에 의해 구분
    # 리터럴 규칙으로 \b = backspace의미 -> 단어 구분자임을 알리기 위해 r'\bclass\b' 처럼 Raw String 알림

p = re.compile(r'\bclass\b') # 앞뒤가 whitespace로 구분된 class라는 단어와 매치됨
print(p.search('no class at all'))
print(p.search('the declassified algorithm')) 
# class 문자열이 포함되어 있지만 whitespace로 구분된 단어가 X -> 매치 X
print(p.search('one subclass is'))

# \B 메타문자 : \b 메타문자와 반대, whitespace로 구분된 단어가 아닌 경우에만 매치
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
print(p.search('the declassified algorithm')) 
# class 앞 뒤에 whitespace가 하나라도 있는 경우 -> 매치 X
print(p.search('one subclass is'))

p = re.compile(r'\Bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm')) 
# class  앞에는 공백 X, 뒤에 whitespace가 있는 경우 -> 매치
print(p.search('one subclass is'))
