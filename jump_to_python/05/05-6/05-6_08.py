# time : 시간과 관련된 모듈

# time.time() : UTC를 사용하여 현재 시간을 실수 형태로 반환하는 함수
import time
a = time.time()
print(a)

# time.localtime : time.time() 이 돌려준 실수값을 사용해서 연도, 월, 일, 시, 분, 초의 형태로 바꾸어주는 함수
import time
a = time.time()
b = time.localtime(a)
print(b)

# time.asctime : time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수
a = time.asctime(b)
print(a)

# time.ctime() : time.asctime(time.localtime(time.time()))을 간편하게 표시
# 항상 현재시간만 돌려줌
import time
a = time.ctime()
print(a)

# time.strftime('출력할 형식포맷코드', time.localtime(time.time())) : 시간에 관계된 것을 세밀하게 표현하는 여러가지 포맷코드 제공

## 시간에 관계된 것을 표현하는 포맷코드 ##
# %a : 요일 줄임말 : Mon
# %A : 요일 : Monday
# %b : 달 줄임말 : Jan
# %B : 달 : January
# %c : 날짜와 시간 출력 : 06/01/01 17:22:21
# %d : 날(day) : [01,31]
# %H : 시간(hour)-24시간 출력형태 : [00,23]
# %I : 시간(hour)-12시간 출력형태 : [01,12]
# %j : 1년 중 누적 날짜 : [001, 366]
# %m : 달 : [01, 12]
# %M : 분 : [01, 59]
# %p : AM or PM : AM
# %S : 초 : [00, 59]
# %U : 1년 중 누적 주-일요일을 시작으로 : [00, 53]
# %w : 숫자로 된 요일 [0(일요일), 6]
# %W : 1년 중 누적 주-월요일을 시작으로 : [00, 53]
# %x : 현재 설정된 로케일에 기반한 날짜 출력 : 06/01/01
# %X : 현재 설정된 로케일에 기반한 시간 출력 : 17:22:21
# %Y : 년도 출력 : 2001
# %Z : 시간대 출력 : 대한민국 표준시
# %% : 문자 : %
# %y : 세기 부분을 제외한 년도 출력 : 01

import time
a = time.strftime('%x', time.localtime(time.time()))
print(a)

a = time.strftime('%c', time.localtime(time.time()))
print(a)

a = time.strftime('%U', time.localtime(time.time()))
print(a)

a = time.strftime('%Z', time.localtime(time.time()))
print(a)

a = time.strftime('%W', time.localtime(time.time()))
print(a)

a = time.strftime('%m', time.localtime(time.time()))
print(a)

a = time.strftime('%M', time.localtime(time.time()))
print(a)

a = time.strftime('%H', time.localtime(time.time()))
print(a)

# time.sleep :  주로 로프 안에서 많이 사용, 일정 시간 간격을 두고 루프 실행 가능

import time
for i in range(10):
    print(i)
    time.sleep(1) # 1초 간격으로 0부터 9까지 숫자 출력, 실수 형태 인수 사용가능

import time
for i in range(20):
    print("루프를 실행한지 %s 초가 지났습니다." % ((0.5) * i))
    time.sleep(0.5)