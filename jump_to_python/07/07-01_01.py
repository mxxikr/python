# 1. 전체 텍스트를 공백 문자로 나눔 -> split
# 2. 주민번호 형식인지 판단
# 3. 주민번호 형식이라면 뒷자리를 * 로 변환
# 4. 나눈 단어를 다시 조립 -> join

data = """park 800905-1049118
kim 700905-1059119""" # data 변수 지정 (""" : 여러줄로 된 문자열)

result = [] # result 변수 지정
for line in data.split("\n"): # 줄바꿈 구분 기호("\n")를 사용하여 문자열 분할
    word_result = [] # word_reult 변수 지정
    #park 800905-1049118
    #kim 700905-1059119
    for word in line.split(" "): # 분할한 문자열을 공백(" ")기준을 분할 -> park,800905-1049118
        #park
        #800905-1049118
        #kim
        #700905-1059119
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit(): 
            # 분할한 문자열길이가 14개고 0~5자리까지 숫자인 문자열 그리고 7~ 끝까지 숫자인 문자열이면
            #800905-1049118
            #700905-1059119
            word = word[:6] + "-" + "*******" #0~5자리까지 숫자인 문자열 + "-" + "*******"인 word 변수 지정
            #800905-*******
            #700905-*******
        word_result.append(word) #word_result 리스트에 word 변수 추가
        print(word_result)
    result.append(" ".join(word_result)) # word_result 요소사이에 " "
    #[' ', 'park 800905-*******', 'kim 700905-*******', '']
print(result)
print("\n".join(result)) # result 요소 사이에 줄바꿈 