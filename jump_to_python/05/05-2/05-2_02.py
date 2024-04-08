# module : 함수나 변수 또는 클래스를 모아놓은 파일
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__=="__main__":
    print(add(1, 4))
    print(sub(5, 2))

#import 명령어 : 이미 만들어 놓은 파이썬 모듈 사용할 수 있게 함 (현재 디렉터리에 있는 파일 or 파이썬 라이브러리가 저장된 디렉터리 안 모듈만)

#__name__ 변수: 파이썬이 내부적으로 사용하는 특별한 변수
    # 직접 파이썬 파일을 실행할 경우 __name__변수에는 __main__값 저장
    # 파이썬 셸에서 실행할 경우 __name__변수에는 모듈 이름값 저장
