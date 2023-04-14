
n = int(input())
buildings = [int(x) for x in input().strip().split(" ")]

res = 0
curr_h = 0
for i in buildings:
    res += abs(i-curr_h)
    if i != 0:
        res += 1
    curr_h = i
res += curr_h # ajoute la derniere facade

print(res)
