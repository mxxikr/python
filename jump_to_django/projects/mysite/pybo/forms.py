from django import forms
from pybo.models import Question, Answer, Comment

class QuestionForm(forms.ModelForm): # ModelForm을 상속받은 QuestionForm 클래스
    class Meta: # 내부 클래스
        model = Question
        fields = ['subject', 'content']
        labels = { # 한글로 표시하고 싶을 경우 label 속성 지정
            'subject': '제목', 
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']

class CommentForm(forms.ModelForm): # 댓글 등록 시 사용
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '댓글내용',
        }