from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentForm
from ..models import Question, Answer, Comment

@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    """
    pybo 질문댓글등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            # Comment 모델의 question 속성에 질문 객체 저장
            comment.question = question 
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('pybo:detail', question_id=comment.question.id), comment.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'pybo/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    """
    pybo 질문댓글수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=comment.question.id)
    # POST 방식일 경우
    if request.method == "POST": 
        # 입력된 값으로 댓글 업데이트
        form = CommentForm(request.POST, instance=comment) 
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            # 업데이트 시 수정일시 반영
            comment.modify_date = timezone.now() 
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('pybo:detail', question_id=comment.question.id), comment.id))
    # GET 방식일 경우            
    else: 
        
        form = CommentForm(instance=comment) 
    context = {'form':form}
    return render(request, 'pybo/comment_form.html', context)

@login_required(login_url="common:login")
def comment_delete_question(request, comment_id):
    """
    pybo 질문댓글삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다.')
        return redirect('pybo:detail', question_id=comment.question.id)
    else:
        comment.delete()
    # 댓글 삭제 시 댓글이 있던 상세화면으로 리다이렉트
    return redirect('pybo:detail', question_id=comment.question.id) 

@login_required(login_url="common:login")
def comment_create_answer(request, answer_id):
    """
    pybo 답글댓글 등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            # answer를 통해 question 참조
            return redirect('{}#comment_{}'.format(
                resolve_url('pybo:detail', question_id=comment.answer.question.id), comment.id))
    else:
        form = CommentForm()
    context = {'form': form }
    return render(request, 'pybo/comment_form.html', context) # 질문 댓글에서 사용한 CommentForm과 comment_form.html 파일 재활용 가능

@login_required(login_url="common:login")
def comment_modify_answer(request, comment_id):
    """
    pybo 답글댓글 수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=comment.answer.question.id)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('pybo:detail', question_id=comment.answer.question.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form':form}
    return render(request, 'pybo/comment_form.html', context)

@login_required(login_url="common:login")
def comment_delete_answer(request, comment_id):
    """
    pybo 답글댓글 삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다.')
        return redirect('pybo:detail', question_id=comment.answer.question.id)
    else:
        comment.delete()
    return redirect('pybo:detail', question_id=comment.answer.question.id)