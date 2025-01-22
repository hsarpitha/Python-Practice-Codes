for y in range(1,11): #-->global scope
    z = 200

def disp(a): #-->block scope
    print(a) #50
    y = 100
    print(y)#not 100

disp(50)
print(y) #10
print(z) #200
# print(a) #Error


# Explain Login required Decorator
# Explain diff types of request
# Deleting nth Node
