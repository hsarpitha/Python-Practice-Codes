class MathOperations:
    @staticmethod
    def add_nums(a, b): #self is not required -- without creating object we can access
        return a + b
    def calci(self):
        pass
#static methods can access using class name or object referance of class
result = MathOperations.add_nums(5, 3)
print(result)

math_op = MathOperations() 
print(math_op.add_nums(10, 5)) #access using an object referance