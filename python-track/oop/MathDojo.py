class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        if type(num) == int or type(num) == float:
            self.result += num
        else:
            for val in num:
                self.result += val
        if nums:
            for val in nums:
                if type(val) == int or type(val) == float:
                    self.result += val
                else:
                    for num in val:
                        self.result += num
        return self

    def subtract(self, num, *nums):
        if type(num) == int or type(num) == float:
            self.result -= num
        else:
            for val in num:
                self.result -= val
        if nums:
            for val in nums:
                if type(val) == int or type(val) == float:
                    self.result -= val
                else:
                    for num in val:
                        self.result -= num
        return self

md = MathDojo()

print md.add(2).add(2, 5).subtract(3, 2).result
md.result = 0 #the one thing I don't like about my code is I have to reset result between calls
print md.add([1], 3, 4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3]).result
md.result = 0
print md.add((1), 3, 4).add((3, 5, 7, 8), (2, 4.3, 1.25)).subtract(2, (2, 3), (1.1, 2.3)).result
