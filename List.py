'''
1. In list we can store Homogeneous as well as Hetrogeneous Data.
2.In list we can store Duplicate Values.
3.List is an Ordered Collection of Data: Order of insertion will remain as it
is in the Output.
4.Lists are Mutalble : Once we declare the list we can modify it.
'''

li1 = [10,20,30,44,55,True,'Kodnest',60]
print(li1, type(li1))

#append(): Will add element at the end of the list
li1.append(300)
print(li1)

#insert(index, element):insert an ele. at specified index.
li1.insert(1, 15)
print(li1) #[10,20,30,44,55,True,'Kodnest',60, 300]

#remove(ele) : Remove the first occurance of the specified ele.
li1.remove(60)
print(li1) #[10,20,30,44,55,True,'Kodnest',60, 300]

#in and not in Operator:
print(2000 in li1) #False
print('Kodnest' in li1) #True

#pop():Without argument will delete and return last ele. fromm list
removed_ele = li1.pop()
print(removed_ele) # 300
print(li1) #[10,20,30,44,55,True,'Kodnest',60]

#pop(index):With argument will delete the ele. at specified index
removed_ele = li1.pop(4)
print(removed_ele) # 55
print(li1) #[10,20,30,44, True,'Kodnest',60]

#del keyword
del li1[1]
print(li1) #[10, 30, 44, True,'Kodnest',60]


del li1
print(li1)# Error: name 'li1' is not defined