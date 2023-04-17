MOD = 7+10**9
n = int(input())+1
a,b,p,q = 1,0,0,1
while n>0:
    if n%2==0:
        qq = q*q
        p, q = (p*p + qq) % MOD, (qq + 2*p*q) % MOD
        n /= 2
    else:
        aq = a*q
        a, b = (aq + p*a + q*b) % MOD, (b*p + aq) % MOD
        n -= 1
print(b)