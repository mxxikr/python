x, r = map(float, input("다른 진수로 변환할 10진수 숫자와 변환할 진수를 입력하세요 : ").split())
remain = ""
result = []

decimal_x = x - int(x)
decimal_result = []

# 정수 부분 계산
while (int(x) != 0):
    remain = int(x) % int(r)

    if int(r) == 16 and remain >= 10:
        if remain == 10:
            remain = "A"
        elif remain == 11:
            remain = "B"
        elif remain == 12:
            remain = "C"
        elif remain == 13:
            remain = "D"
        elif remain == 14:
            remain = "E"
        elif remain == 15:
            remain = "F"

    result.append(str(remain))
    x = int(x) // int(r)

# 소수 부분 계산
remain = ""

while (decimal_x != 0):
    remain = decimal_x * r
    
    if r == 16 and remain >= 10:
        if remain == 10:
            remain_hex = "A"
        elif remain == 11:
            remain_hex = "B"
        elif remain == 12:
            remain_hex = "C"
        elif remain == 13:
            remain_hex = "D"
        elif remain == 14:
            remain_hex = "E"
        elif remain == 15:
            remain_hex = "F"

    if r == 16:
        decimal_result.append(str(remain_hex))
    else:
        decimal_result.append(str(int(remain)))
    decimal_x = remain - int(remain)

result_str = ''.join(result[::-1])
decimal_result_str = ''.join(decimal_result)

if decimal_result_str:
    result_str += "." + decimal_result_str

print("입력한 10진수의 정수 부분을 {} 진수로 변환 값은 {} 입니다.".format(int(r), result_str))