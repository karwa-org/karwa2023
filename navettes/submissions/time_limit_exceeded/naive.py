n, m = map(int, input().split())

ans = 0
while n > 0:
    ans += 1
    n -= m

print(ans)