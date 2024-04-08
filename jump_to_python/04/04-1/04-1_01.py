def add_many(*args): # * :매개변수(arguments) 이름앞에 * 붙이면 입력값 전부 모아서 튜플로 만들어줌
    result = 0
    for i in args:
        result = result + i
    return result

result  = add_many(1, 2, 3)
print(result)

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)