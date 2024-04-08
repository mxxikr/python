from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):    
    """
    author 필드, voter 필드에 related_name 옵션 추가 시
    특정 사용자가 작성한 질문 얻기 위한 코드(some_user.author_question.all()) 사용 가능
    """
    subject = models.CharField(max_length=200)                                                      
    content = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_question")                                                                    
    create_date = models.DateTimeField() 
    modify_date = models.DateTimeField(null=True, blank=True)
    
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject + ":" + str(self.id)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_answer")
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    voter = models.ManyToManyField(User, related_name='voter_answer')

    def __str__(self):
        return self.content
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    content = models.TextField()
    create_date = models.DateTimeField() 
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE) 
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE) 

    def __str__(self):
        return self.content