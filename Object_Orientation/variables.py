class Bank:
    #class variable
    bank_name = 'SBI'
    def __init__(self, name, age, balance):
        #instance variables -- copy for 
        self.user_name = name
        self.age = age
        self.user_balanace = balance
    
    def get_info(self):
        print(f'''User Name is: {self.user_name} and 
            User Balanace: {self.user_balanace}
            for Bank: {Bank.bank_name}''')  #{self.bank_name} also write like this

b1 = Bank('Arpi',23,56000)

print(b1.bank_name) #SBI
print(Bank.bank_name) #SBI
b1.get_info()