#def
def is_odd(name):
    if name % 2 == 1:
        return True
    else:
        return False
a = is_odd(3)
print(a)

a = is_odd(4)
print(a)

#lambda
is_odd = lambda name: True if name % 2 ==1 else False

a = is_odd(3)
print(a)

a = is_odd(4)
print(a)