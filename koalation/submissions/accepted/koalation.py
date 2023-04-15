nbrs = [int(i) for i in input().split()]

primes = [2, 3]

def isPrime(n):
    for i in primes:
        if i*i > n:
            break
        if i%n == 0:
            return False
    return True

for j in range(10000):
    if isPrime(5 + j*6):
        primes.append(5 + j*6)
    if isPrime(7 + j*6):
        primes.append(7 + j*6)


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
            nbrs[i] = (p, p)
nbrs.sort()
print(' '.join(map(lambda x: str(x[1]), nbrs)))
