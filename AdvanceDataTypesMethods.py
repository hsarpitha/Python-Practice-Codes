# li1 = list(5)
# print(li1) #'int' object is not iterable

# list() method only accepting iterable objects as argument

li1 = list('KOD')
print(li1) #['K','o','d']

li2 = list((10,20))
print(li2)

li3 = list({100,200})
print(li3) #[200, 100]

li4 = list({'Name':'Arna','Age':22})
print(li4) #['Name', 'Age'] -- if you are go with dict() only list of keys are printed

li5 = list(range(1,11))
print(li5) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#tuple() -- method accepts iterable objects
#tuple(iterable_Object)
tup1 = tuple([10,20,30]) #list to tuple conversion
print(tup1) #(10, 20, 30) 
tup2 = tuple({100,200}) #set to tuple
print(tup2) #(200, 100)
tup3 = tuple(range(1,11)) #range to tuple
print(tup3) #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tup4 = tuple('Kodnest') #string to tuple
print(tup4) #('K', 'o', 'd', 'n', 'e', 's', 't')
tup5 = tuple({'name':'priya','age':23}) #dict to tuple
print(tup5) #('name', 'age')

#set(iterable_object):
s1 = set([10,20,20,30])
print(s1) #{10, 20, 30} duplicate will be deleted convert to set

#dict(iterable_object:key:value)
d1 = dict([['name','Priya'],['Age',22]])
print(d1) #{'name': 'Priya', 'Age': 22}
d2 = dict((('name','Arna'),('Age',23))) #Using tuple as 2D array
print(d2) #{'name': 'Arna', 'Age': 23}
