li = input('Enter space seperated Elements')
print(li, type(li))#10 20 30 40 <class 'str'>
li = li.split()
print(li) #['10', '20', '30', '40']
li = list(map(int,li))
print(li) #[10, 20]

# print('K-o-d'.split()) #['K', 'o', 'd'] #['K-o-d']

#We can write it in single line code --
tup = tuple(map(int,input('Enter Space seperated Elements ').split()))
print(tup) #(10, 20, 30, 40, 50)

#Sample Input - 10, 11, 12, 13, 14
li = list(map(int,input().split()))
print([i for i in li if i%2 == 0]) #[10, 12, 14]