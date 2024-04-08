#eval(expression) : 실행가능한 문자열을 입력 받아 문자열을 실행한 결괏값을 돌려주는 내장함수
# 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용

a = eval('1+2')
print(a)

a = eval("'hi'+'a'")
print(a)

a = eval('divmod(4, 3)')
print(a)