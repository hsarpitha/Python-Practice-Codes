'''Dict is Mutable.'''
d1 = {'name':'Arna','age':'21','phone':2334565,'age ':23}
print(d1,type(d1)) #{'name': 'Arna', 'age': '23', 'phone': 2334565}<class 'dict'>

#In dict we cannot store duplicate keys.
d1['name'] = 'Arpi'
print(d1) #{'name': 'Arpi', 'age': '21', 'phone': 2334565}

#In dict we can store duplicate values.
marks = {'Sci':85,'Maths':85} #Allowed

for i in d1.keys():
    print(i)

for i in d1.values():
    print(i)

for i in d1.items():
    print(i)

