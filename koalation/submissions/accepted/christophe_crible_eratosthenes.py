n, nbrs = int(input()), list(map(int, input().split()))
bound = max(nbrs)+1
primes = []
is_prime = [True] * bound
for i in range(2, bound):
    if is_prime[i]:
        primes.append(i)
        for j in range(i*i, bound, i):
            is_prime[j] = False

for i, n in enumerate(nbrs):
    if n == 1: nbrs[i] = (1,1)
    else:
        for p in primes:
            if n % p == 0:
                nbrs[i] = (p, n)
                break
nbrs.sort()
print(' '.join(map(lambda x: str(x[1]), nbrs)))