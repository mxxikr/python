from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin): # 제목으로 질문을 검색할 수 있도록 검색 항목 추가
    search_fields = ['subject'] # ['subject'] field 별로 필터링

admin.site.register(Question, QuestionAdmin) # Question 모델을 장고 Admin에 추가

# Register your models here.