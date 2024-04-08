# 특정 디렉터리의 모듈을 * 사용하여 import 할때에는 
# 해당 디렉터리의 __init__.py파일에 __all__ 변수 설정하고 
# import 할 수 있는 모듈 정의해야함

__all__ = ['echo']
# __all__ : sound 디렉터리에서 * 기호를 사용하여 import할 경우 
# 이곳에 정의된 echo 모듈만 import됨

# __all__ 과 상관없이 무조건 import 되는 경우는 
# from의 마지막 항목인 c가 모듈인 경우
