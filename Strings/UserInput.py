#input() will always takes an input as a string:
# Division result will always be of type float.
num1 = int(input('Enter num1'))
#print('Value of num1 is:',num1,'Data Type of num1 is:', type(num1))
num2 = int(input('Enter num2'))
print(f'Addition of {num1} and {num2} is: {num1+ num2}')
print(f'Subtraction of {num1} and {num2} is: {num1 - num2}')
print(f'Multiplication of {num1} and {num2} is: {num1 * num2}')
print(f'Division of {num1} and {num2} is: {num1 / num2}') # 0.5