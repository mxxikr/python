"""
함수 solution은 정수 n을 매개변수로 입력받습니다. 
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
예를들어 n이 118372면 873211을 리턴하면 됩니다.

n은 1이상 8000000000 이하인 자연수입니다.
"""

def solution(n):
    tmp = list(str(n))
    tmp.sort(reverse=True) # 기존 리스트 내림차순 정렬
    
    return int("".join(tmp)) # 리스트 문자열 변환 후 정수 변환

solution(118372)