'''
1.In Tuple we can store Homogeneous as well as Heterogeneous Data.
In tuples we can store Duplicates.
Tuples are ordered collection of data.
Tuples are Immutable: Once we declare the tuple we cannot modify it.
'''

tup1 = (10, 22.55, 'Kodnest', True, 10)
print(tup1)
# tup1.append(500)
# tup1.remove(55)
# del tup1[2]
#Deletes the complete tup1 object
del tup1
# print(tup1) #Error

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1+t2
print(t3) #(1, 2, 3, 4, 5, 6)

# Create a Singleton Tuple:
tup = (10,) # we have give ',' tup with string with out comma <class 'int'>
print(tup,type(tup)) #<class 'tuple'>

new_tup = (10,20,30,40)
# ele1 = new_tup[0] instead of this way
ele1,ele2,ele3,ele4 = new_tup
print(f"Value of ele1",ele1)

