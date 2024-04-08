# python sequence type(열거형 타입)
    # mutable sequence : list

# 많은 값을 하나의 리스트에 저장 -> 연산 가능
# value를 열거

days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(days)
print(type(days))
print("Mon" in days)
print(days[3])
print(len(days)) # 리스트의 길이
print(days)
days.append("Sat") # list는 수정 가능
print(days)
days.reverse() # 역방향
print(days)