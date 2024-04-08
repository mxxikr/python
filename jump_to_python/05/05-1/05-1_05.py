class Calculator: # class 과자틀 -> 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    def sub(self, num):
        self.result -= num
        return self.result
# 객체(object) 과자틀에 의해서 만들어진 과자 -> 클래스로 만든 피조물
cal1 = Calculator()  #cal1 = 객체
cal2 = Calculator()  # class로 만든 객체는 고유한 성격을 가짐 
                     # -> 동일한 클래스로 만든 객체들은 서로 영향을 주지 않음


print(cal1.add(3))
