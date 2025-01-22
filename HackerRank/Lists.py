li = []
n = int(input())
for i in range(n):
    # command, *values['inser','0','5']
    command, *values = input().split()  #'remove 30' /'print'/ 'inser 0 5'
    values = list(map(int,values))  #convert string into int
    if (command == 'insert'):
        li.insert(values[0],values[1])
    elif (command == 'print'):
        print(li)
    elif (command == 'remove'):
        li.remove(values[0])
    elif (command == 'append'):
        li.append(values[0])
    elif (command == 'sort'):
        li.sort()
    elif (command == 'pop'):
        li.pop()
    elif (command == 'reverse'):
        li.reverse()
