class Student:
    def cook(self):
        print('Student is cooking')
    def play(self): #Inherited method
        print('Playing cricket')

class Employee(Student):
    def work(self): #Specialized method
        print('Employee is working')
    def cook(self): #Overriden method
        print('Employee is cooking')

e = Employee()
e.play()

'''
work() : Specialized method: Only in child class
play() : Inherited method: USed as it is in child class
cook() : Overriden method: Change implementation in child class
'''