# class Calculator:
    # def calculate(self,a,b):
        # print('Calculate result of a and b')

class Add:
    def calculate(self, a, b):
        print('Addition:', a+b)

class Sub:
    def calculate(self, a, b):
        print('Subtraction:', a-b)

class Mul:
    pass

# Duck Typing :
def permit(ref,a,b):
    if type(ref).__name__=='Mul':
        print('Mul Class does Not have calculate()')
    else:
        ref.calculate(a,b)
permit(Add(),10,20) #Addition: 30
permit(Sub(),20,10) #Subtraction: 10
permit(Mul(),10,2) #Mul Class does Not have calculate()

'''
1.ref wont check the type of object.
2.ref only give importance to the calculate method
3.ref only gives importance to the methods of object.
'''

# ref = Add()
# ref.calculate(2,5) #7

# ref = Sub()
# ref.calculate(20,10) #10