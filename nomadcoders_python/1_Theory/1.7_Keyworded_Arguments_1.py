# Keyworded_Arguments : 위치에 따라 정해지는게 아니라 argument의 이름으로 쌍을 이룸

def plus(a, b):
    return a - b

result = plus(b=30, a=54) # 인자의 위치에 상관없이 이름에 따라 결정됨
print(result)