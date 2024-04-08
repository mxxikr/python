# os.walk : 하위 디렉터리 검색을 쉽게 해주는 함수
# 시작 디렉터리부터 시작하여 하위 모든 디렉터리를 차례대로 방문하게 해주는 함수

import os

for (path, dir, files) in os.walk("f:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s%s" % (path, filename))