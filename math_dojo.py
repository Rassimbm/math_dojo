# Create a Python class called MathDojo that has one attribute result
class Mathdojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self
    
    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self
    
resul_1 = Mathdojo()
x = resul_1.add(2,3,5,6).subtract(2,9,3,1).result
print(x)