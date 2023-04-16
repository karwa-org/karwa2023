n, nbrs = int(input()), list(map(int, input().split()))
for i, n in enumerate(nbrs):
    if n == 1: nbrs[i] = (1,1)
    p = 2
    while p <= n:
        if n % p == 0:
            nbrs[i] = (p, n)
            break
        else:
            p += 1
nbrs.sort()
print(' '.join(map(lambda x: str(x[1]), nbrs)))