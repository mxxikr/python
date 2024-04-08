def plus(a, b): # 두개 인자 필요
    print(a + b)

def minus(a, b): # 두개 인자 필요
    print(a - b)

def error_fix(a, b=0): # b = 0  default value -> b값이 없다면 0을 대입하라
    print(a - b)


plus(2, 5)
minus(2, 5)
error_fix(2) # b인자 전달하지않음


# 대부분의 함수들은 외부에서 input 받아서 사용 ex)a, b