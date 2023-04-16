from functools import cmp_to_key
n = int(input())
a = list(map(int, input().split()))

mx = max(a)

div = [i for i in range(mx+1)]
for i in range(2, mx):
    if div[i] != i:
        continue
    j = i*i
    while j <= mx:
        if div[j] == j:
            div[j] = i
        j += i

def comp(el1, el2):
    res = div[el1] - div[el2]
    if res != 0:
        return res
    return el1 - el2


print(" ".join(map(str, sorted(a, key=cmp_to_key(comp)))))
