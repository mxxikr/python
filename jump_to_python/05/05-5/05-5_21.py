 # open(filename, [mode]) : "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 돌려주는 함수
 # 읽기 방법 생략 시 기본값인 읽기전용 모드(r)로 파일 객체를 만들어 돌려줌

# w : 쓰기 모드로 파일 열기
# r : 읽기 모드로 파일 열기
# a : 추가 모드로 파일 열기
# b : 바이너리 모드로 파일 열기


f1 = open("binary_file", 'rb') # rb : 바이너리 읽기 모드
f2 = open("read_mode.txt") 
f3 = open("read_mode.txt", 'r') 
f4 = open("append_mode.txt", 'a')

