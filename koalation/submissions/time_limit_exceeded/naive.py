prime_numbers = [2]
ls = [int(i) for i in input().split()]

# this part just precompute all primes between 2 and 10000 since 1 and 0 are not primes
def isPrime(n):
    for i in prime_numbers:
        if n%i == 0:
            return False
        if i**2 > n:
            break
    return True

def preComputePrimes():
    for i in range(3, 10000):
        if isPrime(i):
            prime_numbers.append(i)

preComputePrimes()
            
# this function try to divide n by increasing prime numbers so the first one to divide is the lowest 
def getLowestPrimeFactor(n):
    if n == 1:
        return 1
    else:
        for i in prime_numbers:
            if n%i == 0:
                return i
        return n

factor_ls = [getLowestPrimeFactor(i) for i in ls]

def custComp(i, j):
    x_ = factor_ls[i]
    y_ = factor_ls[j]
    x = ls[i]
    y = ls[j]
    if x_ > y_: return True
    elif x_ == y_:
        if x > y: return True
        else: return False
    else: return False

def primeSort():
    for i in range(len(ls)):
        x = ls[i]
        x_ = factor_ls[i]
        j = i
        while j > 0 and custComp(j-1, j):
            ls[j], ls[j-1] = ls[j-1], ls[j]
            factor_ls[j], factor_ls[j-1] = factor_ls[j-1], factor_ls[j]
            j -= 1;

            
primeSort()
print(" ".join([str(i) for i in ls]))
