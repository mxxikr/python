# 결과를 얻고 그 결과를 변수에 저장하는 함수를 원함
def p_plus(a, b):
    print(a + b) # 결과를 콘솔에 출력만함

def r_plus(a, b):
    return a + b # 함수안에서 return을 해서 함수 밖으로 반환
# returns은 함수종료 기능을 갖고 있음

#p_result = p_plus(2, 4) # None
r_result = r_plus(2, 4) # 6

#print(p_result)
print(r_result)
# p_result = None 아무 값도 아님
# return 키워드 사용시, 함수 호출할때 함수가 return 값으로 치환됨