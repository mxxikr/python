def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

a = avg_numbers(10, 20)
print(a)

a = avg_numbers(1, 2)
print(a)

a = avg_numbers(1, 2, 3, 4, 5)
print(a)