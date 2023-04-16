n = int(input())

mod = int(1e9) + 7

x = y = 1

for i in range(2,n+1):
    x, y = (x + y) % mod, x

print(x)