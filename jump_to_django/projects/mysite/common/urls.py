from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# 로그인 기능 django.contrib.auth앱 사용해 로그인 기능 구현

app_name = 'common'

urlpatterns = [                                 # registration 디렉터리가 아닌 common 디렉터리에서 login.html 파일 참조
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'), # django.contrib.auth 앱 LoginView 클래스 사용
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'), # 로그인 화면에서 회원가입 링크 클릭시 views.signup 함수 실행
]                                             

