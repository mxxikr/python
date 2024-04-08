from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

def signup(request):
    """
    계정생성
    """
    if request.method == "POST": # POST 요청인 경우 
        form = UserForm(request.POST) # 화면에서 입력한 데이터로 새로운 사용자 생성
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # 회원가입 화면에서 입력한 아이디 값 얻기 위해 사용하는 함수
            raw_password = form.cleaned_data.get('password1') # 회원가입 화면에서 입력한 패스워드 값 얻기 위해 사용하는 함수
            user = authenticate(username=username, password=raw_password) # 회원가입 완료 후 자동로그인 위해 authenticate,login 함수 사용
            login(request, user) # authenticate,login 함수 : django.contrib.auth 패키지에 있는 함수로 사용자 인증과 로그인 담당ㄴ
            return redirect('index')
    else: # GET 요청인 경우 
        form = UserForm() # common/signup.html 화면을 반환
    return render(request, 'common/signup.html', {'form': form})

# 오류 내용 담고 있는 exception 변수 추가
def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'common/404.html', {})