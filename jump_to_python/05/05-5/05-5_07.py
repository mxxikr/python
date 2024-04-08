# enumerate : 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력받아 인덱스 값을 포함하는 enumerate 객체를 돌려줌

for i, name in enumerate(['body', 'foo', 'bar', '']):
    print(i, name)

    #for문과 함께 사용하면 자료형의 현재순서(index)와 그 값을 알 수 있음
    