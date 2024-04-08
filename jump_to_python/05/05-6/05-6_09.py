# calender : 파이썬에서 달력을 볼 수 있게 해주는 모듈

# calendar.calendar(연도) : 그 해 전체 달력 볼 수 있음
import calendar
a = calendar.calendar(2020)
print(a)

# calender.prcal(연도) : 그 해 전체 달력 볼 수 있음
print(calendar.prcal(2020))

# calendar.prmonth(연도, 월) : 해당 연도의 해당 월 달력만 보여줌
print(calendar.prmonth(2020, 11))

# calender.weekday(연도, 월, 일) : 그 날짜에 해당하는 요일 정보를 돌려줌
print(calendar.weekday(2020, 11, 15))
# 월:0, 화:1, 수:2, 목:3, 금:4, 토:5, 일:6

# calender.monthrange(연도, 월) : 입력받은 달의 1일이 무슨요일인지, 그 달이 며칠까지 있는지를 튜플형태로 돌려줌
print(calendar.monthrange(2020, 11))

# assigning result of a function call where the function has no return.