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
    pass
a = MoreFourCal(4, 2)
print(a.first)
print(a.second)
print(a.add())
print(a.div())
print(a.sub())
print(a.mul())
