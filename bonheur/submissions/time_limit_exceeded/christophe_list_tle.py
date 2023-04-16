n,k=list(map(int,input().split()))
nbrs = []
for i in map(int,input().split()):
    sub = k-i
    if sub in nbrs:
        print("yes")
        break
    nbrs.append(i)
else:
    print("no")
