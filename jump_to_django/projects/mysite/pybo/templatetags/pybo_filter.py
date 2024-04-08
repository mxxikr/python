import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# 사용자 정의 필터 등록 -> name 인수 생략해 함수이름을 필터 이름으로 사용
@register.filter 
def sub(value, arg): 
    return value - arg 

# @register.filter 애너테이션 적용 시 템플릿에서 해당 함수 필터로 사용
@register.filter
def mark(value):
    # 확장도구 설정
    extensions = ["nl2br", "fenced_code"]
    # 문자열을 HTML 코드로 변환하여 반환
    return mark_safe(markdown.markdown(value, extensions=extensions))