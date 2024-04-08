class FourCal:
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

a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(5, 6)

print(a.mul())
print(a.add())
print(a.sub())
print(a.div())


print(b.mul())
print(b.add())
print(b.sub())
print(b.div())
