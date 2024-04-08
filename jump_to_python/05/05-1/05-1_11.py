#생성자(Constructor) : 객체가 생성될 때 자동으로 호출하는 Method
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


a = FourCal(4, 2)
print(a.first)
print(a.second)
print(a.add())
print(a.div())
print(a.sub())
print(a.mul())

