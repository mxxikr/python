# tempfile 파일을 임시로 만들어서 사용할 때 유용한 모듈

import tempfile
filename = tempfile.mkstemp() # 중복되지않는 임시 파일의 이름을 무작위로 만들어서 돌려줌
print(filename)

import tempfile ### 이해 부족
filename = tempfile.TemporaryFile() # 임시 저장공간으로 사용할 파일 객체를 돌려줌(default : wb모드)
print(filename)
filename.close() # 호출 시 파일 객체는 자동으로 사라짐
