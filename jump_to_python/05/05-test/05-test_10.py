# os 모듈 사용

import os

os.chdir("C:/Users/mxxikr")

a = os.popen("dir")
print(a.read())
