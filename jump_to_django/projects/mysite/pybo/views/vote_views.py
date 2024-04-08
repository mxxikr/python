from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from ..models import Question, Answer

@login_required(login_url='common:login')
def voter_question(request, question_id):
    """
    pybo 질문 추천 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        # 자기 추천 방지
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        # add 함수로 추천인 추가
        # ManyToManyField는 중복을 허락하지 않음 -> 같은 사용자가 하나의 질문 여러번 추천 불가
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)

@login_required(login_url='common:login')
def voter_answer(request, answer_id):
    """
    pybo 답변 추천 등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)