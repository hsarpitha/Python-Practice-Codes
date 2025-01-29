def count_substring(string, sub_string):
    count = 0
    n = len(string) - len(sub_string) + 1
    for i in range(n):
        if(sub_string[i:len(string)+i]==sub_string):
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

