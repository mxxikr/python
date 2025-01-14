"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pybo.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')), 
    path('common/', include('common.urls')), # common 앱의 urls.py 파일을 사용하기 위해 추가
    # /common/으로 시작하는 URL 모두 common/urls.py 파일 참조
    path('', base_views.index),
]

# handler404 변수 설정 -> 404 오류 발생 시 사용자가 정의한 뷰함수 호출
handler404 = 'common.views.page_not_found'