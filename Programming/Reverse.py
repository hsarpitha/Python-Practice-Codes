#reverse() will reverse the original object.
li = [10,5,20,7,4]
print('Before Reverse:',li)
li.reverse()
print('After Reverse:',li) # [4, 7, 20, 5, 10]

#reversed(iterable_object):
li2 = [11,6,8,22]
reverse_li2 = list(reversed(li2)) #[22, 8, 6, 11]
print(li2) #[11, 6, 8, 22]
print(reverse_li2) 

li3 = [1,5,2,9]
new_reverse_li3 = list(reversed(li3)) #-->Creating new revese list
li3.reverse() #-->Reverseing Original List
print(new_reverse_li3) #[9, 2, 5, 1]
print(li3) #[9, 2, 5, 1]

# Reveserd Object returns Iteraror Object