# greedy 문자 : * 

import re

s = '<html><head><title>Title</title>'

a = len(s)
print(a)

print(re.match('<.*>', s).span()) # s변수에서 '<.*>'에 매치되는 객체의 처음과 끝 표시
print(re.match('<.*>', s).group()) # * 메타 문자는 매치할 수 있는 최대 문자열을 모두 소비함(greedy)

# non-greedy : ? 
    # 가능한 가장 최소한의 반복을 수행하도록 도와주는 역할
    # greedy를 제한하고 <html>문자열까지만 소비하도록 하는 방법
    # ?, *?, +?, ??, {m, n}?

print(re.match('<.*?>', s).span()) #?를 사용하면 * greedy 제한 가능
print(re.match('<.*?>', s).group())