'''
1.In set we can store Homogeneous as well as Heterogeneous data.
2.Set is an unorderd collection of data. -- means doen't support
indexing.
3.Set doesn't support indexing of data.
4.In set we can not store duplicates.
5.Sets are mutable. '''
s1 = {10,True,'Kodnest',10,20,55.44}
print(s1,type(s1))  #{True, 20, 55.44, 10, 'Kodnest'} <class 'set'>
# print(s1[0]) Error

#add():Used to add an element in the set.
s1.add(500)
print(s1)   #{True, 20, 500, 'Kodnest', 55.44, 10}

#remove():
s1.remove(55.44)
print(s1)   #{True, 20, 500, 'Kodnest', 10}


s1.pop()
print(s1)   #{20, 500, 10, 'Kodnest'}
#pop():Without index will delete and return one ele.
poped_ele = s1.pop()
print(poped_ele)
print(s1)
#{20, 'Kodnest', 500, 10}
#20
#{'Kodnest', 500, 10}

# del s1[2]#Error
del s1 # delete entire set
