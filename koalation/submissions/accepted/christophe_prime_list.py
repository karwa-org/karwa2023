n, nbrs = int(input()), list(map(int, input().split()))
primes = [2]
for i in range(3, max(nbrs)+1):
    is_prime = True
    for p in primes:
        if i % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

for i, n in enumerate(nbrs):
    if n == 1: nbrs[i] = (1,1)
    else:
        for p in primes:
            if n % p == 0:
                nbrs[i] = (p, n)
                break
nbrs.sort()
print(' '.join(map(lambda x: str(x[1]), nbrs)))