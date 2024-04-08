#상속(inheritance)
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
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

# Method Overriding(덮어쓰기) : 부모클래스에 있는 Method를 동일한 이름으로 다시 만드는 것
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = MoreFourCal(4, 2)
a = SafeFourCal(4, 0)
print(a.div())
