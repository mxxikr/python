# 페이징 : 게시판의 페이지 수를 보여주는 것

# 함수 이름 : getTotalPage
# 입력값 : 게시물의 총건수(m), 한 페이지에 보여줄 게시물 수(n)
# 출력값 : 총 페이지 수 

# 총 페이지 수 : 총 건수 / 한페이지당 보여줄 건수 + 1

def getTotalPage(m, n):
    if m % n == 0:
        return m // n # // : 소수점 아래자리를 버림
    else:
        return m // n + 1 

print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10)) # 총 페이지 수 3이 되어야함 -> 나머지값 0될 때 발생