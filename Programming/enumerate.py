#enumerate() function is used to use both index, element
li = [10, 20, 30]
for ide, ele in enumerate(li):
    print(ide,ele)

li = [10,20,30,40]
for idx, ele in enumerate(li):
    print(f"Index of {ele} is {idx}")

#Write a python programme to print all even index element
for idx, ele in enumerate(li,start=1):
    if idx % 2 == 0:
        print(ele)