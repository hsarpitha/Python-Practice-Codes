d = {}
n = int(input()) #number of studets
for i in range(n):
    name, *score = input().split() #['Malika','10','20']
    score = list(map(float,score))
    d[name] = score
target_name = input()
for name, score in d.items():
    if name == target_name:
        avg = sum(score)/len(score)
print(f"{avg:.2f}")