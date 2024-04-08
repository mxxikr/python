def plus(a, b):
    if type(b) is int or type(b) is float: # b가 숫자(정수, 소수)일 때만 연산
        return a + b
    else: # if 조건에 맞지않으면 전부 else
        return None # error

print(plus(12, "10"))
print(plus(12, 2.5))