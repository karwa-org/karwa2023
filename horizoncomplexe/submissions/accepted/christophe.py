n, hh, ans, height = int(input()), list(map(int,input().split())), 0, 0
for h in hh: ans, height = ans + abs(h-height) + (1 if h > 0 else 0), h
print(ans+h)
