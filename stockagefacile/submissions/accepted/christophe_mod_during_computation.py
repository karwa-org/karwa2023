n = int(input())+1
a,b,p,q = 1,0,0,1
while n>0:
    if n & 1 == 0:
        qq = q*q
        p, q = (p*p + qq), (qq + 2*p*q)
        n = n >> 1
    else:
        aq = a*q
        a, b = (aq + p*a + q*b), (b*p + aq)
        n -= 1
print(b%(7+10**9))