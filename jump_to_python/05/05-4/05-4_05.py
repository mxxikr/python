class Bird:
    def fly(self):
        raise NotImplementedError # 파이썬 내장오류

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()