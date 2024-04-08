# 입력값 : 메모 내용, 프로그램 실행 옵션
# 출력값 : memo.txt
# 필요 기능 : 메모 추가, 메모 조회

import sys

option = sys.argv[1] # sys.argv : 프로그램 실행할 때 입력한 값을 읽어들일 수 있는 라이브러리

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a') # 항상 추가 되어야하므로 a 파일 모드
    f.write(memo)
    f.write('\n') # 줄바꿈 문자
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
