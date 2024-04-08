from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm): # django.contrib.auth.forms 패키지의 UserCreationForm 클래스 상속
    email = forms.EmailField(label="이메일") # email 속성 추가
# UserCreationForm이 기본적으로 가지고 있는 속성에 부가정보인 email 속성 추가하기 위해 UserCreationForm을 상속한 UserForm 생성
    class Meta:
        model = User
        fields = ("username", "email")