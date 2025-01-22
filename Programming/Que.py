li = list(map(int,input().split()))
d = {10:2,20:1,30:1}
# print(d.items)
for num, count in d.items(): #-->Unpacking key:value pair
    print(f"{num} occurs {count} times(s)")
'''
10 occurs 2 times(s)
20 occurs 1 times(s)
30 occurs 1 times(s)
'''

li1 = list(map(int,input().split())) #[1,2,2,3,3,3,4,4,4,4]
d = {}
for i in li:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for num, count in d.items():
    print(f"{num} occurs {count} times(s)")