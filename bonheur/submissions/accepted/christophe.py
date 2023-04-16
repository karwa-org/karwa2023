n,k=list(map(int,input().split()))
nbrs = set()
for i in map(int,input().split()):
    sub = k-i
    if sub in nbrs:
        print("yes")
        break
    nbrs.add(i)
else:
    print("no")
