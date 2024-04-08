# os : 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈

# os.environ : 현재 시스템의 환경변수값을 딕셔너리 객체로 돌려줌
import os
a = os.environ
print(a)
print(a['PATH']) # 시스템의 PATH 환경 변수 내용

# os.system : 시스템 명령어 호출하기
import os
a = os.system("dir") # 시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출
print(a)

# os.popen : 실행한 시스템 명령어의 결괏값을 읽기 모드 형태의 파일 객체로 돌려받기
import os
a = os.popen("dir")
print(a.read()) # 읽어들인 파일 객체의 내용 보기

# os.chdir : 디렉터리 위치 변경하기

# os.getcwd : 현재 자신의 디렉터리 위치 돌려받기
import os
a = os.getcwd()
print(a)

# os.mkdir(d) : 디렉터리 생성
# os.rmdir(d) : 디렉터리 삭제 (비어있는 디렉터리만 삭제 가능)
# os.unlink(f) : 파일을 지움
# os.rename(src, dst) : src라는 이름의 파일을 dst라는 이름으로 변경