import sys

numbers = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력

result = 0

for i in numbers:
    result += int(i)
print(result)
