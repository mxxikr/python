from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
# OR 문 조건으로 사용하기 위해 Q 사용

# views 디렉토리 위의 models.py의 Question 클래스 임포트
from ..models import Question, Answer, Comment

import logging
logger = logging.getLogger(__name__)

def index(request): 
    """
    pybo 목록 출력
    """
    logger.info("INFO 레벨로 출력")
    # 입력 파라미터
    page = request.GET.get('page','1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent') # 정렬기준

    # 정렬
    if so == 'recommend':
        # 정렬 기준 추천순인 경우 추천 수가 큰 것부터 정렬하므로 order_py에 추천수 -num_voter(장고 annotate,Count 함수 사용해 구함) 입력
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == "popular":   
        # 함수에 두 개 이상 인자 전달될 경우 1번째 항목부터 우선순위 매김 => 답변수 같으면 최신순 정렬
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else: # recent
        question_list = Question.objects.order_by('-create_date')
    # 조회

    # 검색
    if kw: 
        # filter 함수에서 모델 필드에 접근 할 때 __ 이용
        # filter 인자로 넘겨줘 조건에 부합하는 데이터 조회 가능
        question_list = question_list.filter(
            # 필드명__icontains : 대소문자 구분 없이 조건값이 포함되는 데이터 가져옴
            # 제목에 kw 문자열 포함되었는지
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw) |
            # 답변 작성한 사람의 이름에 포함되는지 
            Q(answer__author__username__icontains=kw)
        ).distinct()

    # 페이징처리
    # 페이지당 10개씩 보여주기
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page) 

    # 입력으로 받은 page, kw, so값 템플릿 searchForm에 전달하기 위해 추가
    context = {'question_list' : page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    page = request.GET.get('page','1')
    so = request.GET.get('so','reset')

    question = get_object_or_404(Question, pk=question_id)
    answer_list = Answer.objects.filter(question=question).order_by('-create_date')

    paginator = Paginator(answer_list, 10)
    page_obj_a = paginator.get_page(page) 

    if so == 'recommend':
        answer_list = Answer.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == "popular":   
        answer_list = Answer.objects.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    else: 
        answer_list = Answer.objects.order_by('-create_date')
    
    context = {'question' : question, 'page': page, 'answer_list' : page_obj_a, 'so': so }
    return render(request, 'pybo/question_detail.html', context)