n = int(input())
h = list(map(int, input().split()))


ans = h[0]
if n > 1:
    ans += h[-1]

for i in range(1,n):
    ans += abs(h[i] - h[i-1])

ans += sum(h[i] > 0 for i in range(n))

print(ans)
