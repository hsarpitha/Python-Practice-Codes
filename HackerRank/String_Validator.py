#alnum(): Checks for alphabets or numbers or  both(either alphabet or nubers)
s = 'Kodnest123*'
print(s.isalnum()) # False
print('Kodnest'.isalnum()) #True

#isalpha(): Checks for only alphabet
s2 = 'Kodnest'
print(s2.isalpha()) #True
print('code'.isalpha())#True

#isdigit(): Checks for only numbers
print('12'.isdigit()) #True
print('23ASD'.isdigit()) #False

#islower(): Checks for every letter is lower or not
print('apple'.islower()) #True

#isupper(): Checks for is every alphabet is in upper case or not
print('AcsS'.isupper()) #False
print('ABC'.isupper()) #True

#any():
print(any([10,20])) #True
print(any([True,False])) #True
print(any([False,False])) #False

#---------------------------------------------
s = input() #qA2
print(any([i.isalnum() for i in s])) #True
print(any([i.isalpha() for i in s])) #True
print(any([i.isdigit() for i in s]))
print(any([i.islower() for i in s]))
print(any([i.isupper() for i in s]))



