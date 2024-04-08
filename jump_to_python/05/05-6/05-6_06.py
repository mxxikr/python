# glob : 특정 디렉터리에 있는 파일 이름 모두 알아야할 때 사용 -> 디렉터리에 있는 파일들을 리스트로 만들기
# glob(pathname)
import glob # 디렉터리 안의 파일들을 읽어서 돌려줌
a = glob.glob("C:/Users/mxxikr/Python_TEST/*") # *, ? 등 메타문자 사용해 원하는 파일만 읽기 가능
print(a)

import glob
a = glob.glob("C:/Users/mxxikr/*")
print(a)