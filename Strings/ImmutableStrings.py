"""ImmutableString : 
1.Once we Declare the string we cannot modify it,
if we try to modify the string it will create new string.
2. If new string does not have any referance variable then it will be removed.
3. Python internally uses String Interning.
4.String Interning is the process of checking string intern Pool before creating
any new object.
5.When ever we want create new object, Python first will check string intern
pool, wheather, that object already exist or not.
6. When Object already exist in the string intern Records then address of existing
object will be reused.
"""

# s1 = 'Kodnest'
# s2 = s1.upper()      S1 = S1.Upper() Kodnest
# print(s2) KODNEST

# s1 = 'K'
# print(s1, id(s1))

s1 = 'Hello'
s2 = 'World'
print(s1, id(s1))
print(s2, id(s2))

print(s1[0]) # H
print(s1[-1]) # o

print('s1 ID of H:',id(s1[0]))
print('s1 ID of o:',id(s1[-1]))

print('s2 ID of W',id(s2[0])) # same id as s1
print('s2 ID of o:',id(s2[1]))

print('s1 Id of l:',id(s1[2]))
print('s1 ID of l:',id(s1[3]))
print('s2 ID of l:',id(s2[3]))