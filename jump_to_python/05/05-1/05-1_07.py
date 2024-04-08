class FourCal:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result
    def mul(self, num):
        self.result *= num
        return self.result       
    def sub(self, num):
        self.result -= num
        return self.result
    def div(self, num):
        self.result /= num
        return self.result
a = FourCal() # a 객체 만들기, FourCal 클래스의 인스턴스
print(type(a))

print(a.add(3))
print(a.mul(3))
print(a.sub(3))
print(a.div(3))
