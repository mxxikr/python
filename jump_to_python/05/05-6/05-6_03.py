#pickle : 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게하는 모듈

import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f) # dump 함수를 사용 -> 딕셔너리 개체인 data를 파일에 저장
f.close()

import pickle
f = open("test.txt", 'rb')
data = pickle.load(f) # load를 사용 -> 딕셔너리 개체 data를 그대로 불러옴
print(data)

import pickle
f = open("test.txt", 'wb')
data = [1, 2, 3, 4]
pickle.dump(data, f) # dump 함수를 사용 -> 리스트 객체인 data를 파일에 저장
f.close()

import pickle
f = open("test.txt", 'rb')
data = pickle.load(f) # load를 사용 -> 리스트 객체인 data를 그대로 불러옴
print(data)