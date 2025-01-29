li1 = [1,2,3,4,5]
# print(li1)
# sq_list = []
# for i in li1:
    # sq_list.append(i**2)
# print(sq_list) #[1, 4, 9, 16, 25]

#Syntax: [expression for i in iterable_object condition]

duplicate_li1 = [i for i in li1]
print(duplicate_li1) #[1, 2, 3, 4, 5]

even = [i for i in li1 if i%2==0]
print(even) #[2, 4]

sq_list = [i**2 for i in li1]
print(sq_list) #[1, 4, 9, 16, 25]

new_li1 = [ele+2 for ele in li1]
print(new_li1) #[3, 4, 5, 6, 7]

#if and else both in List Comprehension:
#Syntax: ['even' if i%2==0 else 'Odd' for i in li1]

#If we have to write both conditions, before the for loop only write.
#When we have if-else both write it before for loop
even_odd = ['even' if i%2==0 else 'Odd' for i in li1]
print(even_odd) #['Odd', 'even', 'Odd', 'even', 'Odd']

#Multiple for loop inside list comprehension:
#Syntax: [ele for i in li for ele in i] first increment in second for loop then first for loop
li = [[10,20],[30,40],[50,60]]
new_li = [ele for sublist in li for ele in sublist]
print(new_li) #[10, 20, 30, 40, 50, 60]as per requirement


