#Find Ruuner-up Score
li = list (map(int,input().split()))
li = [10,20,40,30,40]
li = list(set(li)) #{10,20,40,30}
# sort()--> wont return anything(None)
li.sort(reverse='True') #[40,30,20,10]
print(li) #[10,20,30,40]
print(li[1]) #30

# 10,20,30,40,20
li = list(map(int, input().split(',')))
# li = [10,20,30,40,20]
li = list(set(li))
li.sort()
print(li[1])

'''
print("Largest Element:",li[-1])
print("Second Largest Element:",li[-2])
print("Smallest Element:",li[0])
print("Second Smallest Element:",li[1])
'''