'''
Method Chaining is the process of calling one method
from another method.
'''
class GrandParent:
    def cook(self):
        print('GrandParent can cook Biriyani')

class Parent(GrandParent):
    def cook(self):
        print('Parent can cook Maggie')
        # super().cook()

class Child(Parent):
    def cook(self):
        print('Child wont cook')
        super().cook()
        super(Parent,self).cook() #Parent class parent will be printed

c = Child()
c.cook() #Child wont cook
# using super() we can get all 3 methods