#dir : 객체가 자체적으로 가지고 있는 변수나 함수 보여줌

a = dir([1, 2, 4]) # 리스트 객체 관련 함수를 보여줌
print(a)

a = dir([{'1':'a'}]) # 딕셔너리 객체 관련 함수를 보여줌
print(a)