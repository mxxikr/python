# 문자열 formatting
def say_hello_format(name, age):
    return f"Hello {name} you are {age} years old"
    #string 안에 변수를 포함시키고 싶으면 문자열 앞에 f(format 의미) {변수} 추가

hello_format = say_hello_format("nico", "12")
print(hello_format)

# + 사용
def say_hello_plus(name, age):
    return "Hello " + name + " you are " + age + " years old"

hello_pluse = say_hello_plus("nico", "12")
print(hello_pluse)

# keyworded arguments
def say_hello_kw(name, age):
    return f"Hello {name} you are {age} years old"

hello_kw = say_hello_kw(age="12", name="nico")
print(hello_kw)

# 문자열 keyworded arguments 사용 X 
def say_hello_u(name, age, are_from, fav_food):
    return f"Hello {name}. you are {age} years old. you are from {are_from}. you like {fav_food}."

hello_u = say_hello_u("nico", "12", "korea", "chicken") # argument가 여러개일 때 순서 기억 필요
print(hello_u)

# 문자열 keyworded arguments 사용 O
def say_hello_nu(name, age, are_from, fav_food):
    return f"Hello {name}. you are {age} years old. you are from {are_from}. you like {fav_food}."

hello_nu = say_hello_nu(age="12", are_from="korea", fav_food="chicken", name="nico") # argument가 여러개일 때 순서 기억 불필요
print(hello_nu)