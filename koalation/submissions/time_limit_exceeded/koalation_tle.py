n, nbrs = int(input()), [int(i) for i in input().split()]

primes = [2, 3]

def isPrime(n):
    for i in primes:
        if i*i > n:
            break
        if i%n == 0:
            return False
    return True

for j in range(2, int(1e6)):
    if isPrime(j):
        primes.append(j)

for i, n in enumerate(nbrs):
    if n == 1: nbrs[i] = (1,1)
    else:
        test = False
        for p in primes:
            if n % p == 0:
                nbrs[i] = (p, n)
                test = True
                break
        if not test:
            nbrs[i] = (p, n)
nbrs.sort()
print(' '.join(map(lambda x: str(x[1]), nbrs)))
