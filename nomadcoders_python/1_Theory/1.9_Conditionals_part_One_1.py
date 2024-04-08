def plus(a, b):
    if type(b) is str: # user gave me a string : condition:
        return None # error
    else:
        return a + b 
# b의 type이 string일 때만 None 반환

print(plus(12, "10"))
print(plus(12, 10))
