n = int(input())+1
sqrtFive = 5**.5
fn = round(((1+sqrtFive)/2)**n/sqrtFive) # can compute up to the ~85th fib number due to double error
print(fn)