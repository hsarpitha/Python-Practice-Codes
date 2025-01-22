li = input().split() #this is a sample
print(li) # ['this', 'is', 'a', 'sample']
s = '-'.join(li)
print(s)  #this-is-a-sample

# --------------------

def split_and_join(line):
    # write your code here
    line = line.split()
    return '-'.join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

