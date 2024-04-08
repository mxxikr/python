def say_hello(name="anonymous"): # argument에 default값 지정
    print("hello", name) # print function 무한대의 인자를 가질 수 있음

say_hello() # 인자없이 함수 호출시 매개변수에 default값 지정 필요
say_hello("nico") # 인자대입

# 대부분의 함수들은 외부에서 input 받아서 사용 ex)name