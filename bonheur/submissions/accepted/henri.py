n,k = map(int, input().split())
t = set(map(int, input().split()))

ok = False
for x in t:
    if(k-x in t):
        ok = True
if ok:
    print("yes")
else:
    print("no")


