#Without input and return statement
def add():
    a = 10
    b = 20
    print('Addition is:',a+b)
add()

#With input and without return statement
def sub(a,b):
    print('Subtraction is:',a-b)

#Without input and with return statement:
def mul():
    return 10 * 20

#With input and with return statement
def div(a,b):
    return a / b

sub(100, 40)
print(mul())
print(div(200,20))