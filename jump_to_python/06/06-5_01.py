# 입력값 : 문서파일
# 출력값 : 탭이 공백으로 출력된 파일
# 기능 : 문서파일 읽기, 문자열 변경

#python tabto4.py src dst

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src) # src에 해당하는 입력파일 읽기
tab_content = f.read() # 입력파일 내용 변수에 저장
f.close()

space_content = tab_content.replace("\t", " "*4)

f = open(dst, 'w')
f.write(space_content)
f.close()