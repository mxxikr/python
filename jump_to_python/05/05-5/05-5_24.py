# range([start,] stop [,step]) :  입력 받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려줌


# 인수가 1개 -> 0부터 시작
a = list(range(5))
print(a)

# 인수가 2개 -> 시작숫자, 끝 숫자(끝 숫자는 범위에 포함 X)
a = list(range(5, 10))
print(a)

# 인수가 3개 -> 숫자 사이의 거리
a = list(range(1, 10 , 2))
print(a)

a = list(range(0, -10 , -1))
print(a)