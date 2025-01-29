class Employee:
    comapany_name = 'code' #Class based variable.
    def __init__(self, name, age, desig):
        self.name = name
        self.age = age
        self.desig = desig

    def login(self, time):
        print(f"{self.name} logged in at {time}")

    def logout(self, time):
        print(f"{self.name} logged out at {time}")

    def work(self, hours):
        print(f"{self.name} worked for {hours}")

    def getDetails(self):
        print(f"Employee Name: ",self.name)
        print(f"Employee Age: ",self.age)
        print(f"Employee Designation: ",self.desig)

#Creating Objects:
e1 = Employee('Arna',23,'Software Developer')
e2 = Employee('Akash',24,'Back End Developer')

e1.getDetails()
e1.login('9 AM')
e1.logout('6 PM')
e1.work('10 Hrs')
print()
e2.getDetails()
e2.login('10 AM')
e2.logout('7 PM')
e2.work('6 Hrs')        