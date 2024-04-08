# threading 모듈 : 스레드를 다루는 모듈
# process : 컴퓨터에서 동작하고 있는 프로그램

# 보통 1개의 프로세스는 한가지일만 함 
# Thread를 사용하면 한 프로세스 안에서 2가지 또는 그 이상의 일을 동시에 수행가능

import time # 시간과 관련된 time 모듈 사용

def long_task(): # 수행하는데 5초의 시간이 걸리는 long_task 함수
    for i in range(5): # 0부터 4까지
        time.sleep(1) # 1초간 대기
        print("working:%s\n" % i )

print("Start")

for i in range(5): # long_task를 5회 수행 
    long_task()

print("End")

# Thread를 사용하면 5초의 시간이 걸리는 long_task 함수를 동시에 실행 가능 -> 시간절약
import time
import threading # Thread 생성하기 위해서는 threading 모듈이 필요

def long_task2():
    for i in range(5): # 0 ~ 4 범위 i값
        time.sleep(1) # 1초 간격으로 출력
        print("working:%s\n" % i)

print("Start")

threads = []
# threading.Thread : 만든 Thread 객체가 동시 작업을 가능하게 함
for i in range(5):
    t = threading.Thread(target=long_task2) # Thread 생성
    threads.append(t)

for t in threads:
    t.start() # Thread 실행

for t in threads:
    t.join() # join으로 해당 Thread가 종료될때까지 대기

print("End")