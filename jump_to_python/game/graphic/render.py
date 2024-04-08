# render.py

#echo 함수 사용할 수 있도록 수정
#graphic 디렉터리의 render 모듈이 sound 디렉터리의 echo 모듈을 사용하고싶을때

from sound.echo import echo_test

def render_test():
    print("render")
    echo_test()

    # relative 한 접근자 -> render.py처럼 모듈안에서만 사용해야함, 인터프리터에서 사용시 SystemError:cannot perform relative import 오류 발생
        # .. : 부모디렉토리
        # . : 현재 디렉토리