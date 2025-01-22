print(bool('Kodnest')) # True
#print(int('Kod')) #Error
print(int('11')) # 11 --->IMP Str(int) --> Int
print(float('22.34')) # 22.34 ---> IMP
print(bool('')) #False
print(bool(0)) #False
print(bool(12)) #True
#print(int('12.23')) #Error
print(int(12.34)) #12

#Taking float value from user and converting it into int 
value = int(float(input('Enter price:Float value')))
print(value, type(value))