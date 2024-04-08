
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname) # 해당 디렉터리에 있는 파일들의 리스트 구함
        for filename in filenames:
            full_filename = os.path.join(dirname, filename) # 디렉터리와 파일 이름 붙여줌
            if os.path.isdir(full_filename): # 파일 디렉터리 구분 
                search(full_filename) # 디렉터리 일 경우 search 함수 호출
            else:
                ext = os.path.splitext(full_filename)[-1] # 파일 이름에서 확장자만 추출
                if ext == '.py':
                    print(full_filename)
    except PermissionError: # 권한 없는 디렉터리에 접근할때 오류 발생 X
        pass # 오류로 종료되지않고 수행

search("f:/")

# 재귀호출 : 자기 자신을 다시 호출하는 프로그래밍 기법
# ex) search함수에서 다시 자기자신인 search 함수 호출

# os.path.join(dirname, filename) : 해당 OS형식에 맞도록 경로 연결
# os.path.isdir(filename) : 파일이 디렉토리인지 검사를 하는 함수
# os.path.splitext(filename) : 입력받은 경로를 확장자 부분과 그 외 부분으로 나눔