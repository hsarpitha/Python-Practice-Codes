# n = 5
# print('*' * n)

rows = 4
col = 5
for i in range(rows):
    for j in range(col):
        print("*", end="")
    print()

print()
#for increasing pattern : inner loop : i+1
for i in range(rows):
    for j in range(i+1):
        print("*", end=" ")
    print()

print()
#for decresing pattern : inner loop : (i, rows)
for i in range(rows):
    for j in range(i,rows):
        print("*", end=" ")
    print()

print()
#right pascal triangle --inner loop of decrsing pattern :(i, rows-1)
for i in range(rows):
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print("*", end=" ")
    print()

print()

#Butterfly pattern:
for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    for j in range(i,rows-1):
        print(" ", end="")
    for j in range(i,rows-1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()
for i in range(rows):
    for j in range(i, rows-1):
        print("*",end="")
    for j in range(i+1):
        print(" ", end="")
    for j in range(i+1):
        print(" ", end="")
    for j in range(i,rows-1):
        print("*", end="")
    print()

for i in range(rows):
    for j in range(i, rows):
        print("-",end="")
    for j in range(i):  # adjust to pyramid shape
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(1,rows):
    for j in range(i+1):
        print("-",end="")
    for j in range(i, rows-1):
        print("*",end="")
    for j in range(i, rows):
        print("*",end="")
    print()
