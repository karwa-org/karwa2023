n = int(input())

m = 10**9 + 7

prev = 0
curr = 1
for i in range(n):
    prev, curr = curr, (prev+curr) % m
print(curr)
