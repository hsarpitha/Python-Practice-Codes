#print('a'.islower()) #True
#print('Kodnest'.isupper()) #False

#s = input() #PythoN ---> pYTHOn

def swapcase(s):
    sample = '' #empty string
    for i in s:
        if i.islower():
            sample = sample + i.upper()
        else :
            sample = sample + i.lower()
    return sample

res = swapcase('PythoN12')
print(res)
