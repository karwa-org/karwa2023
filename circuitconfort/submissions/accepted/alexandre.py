from collections import defaultdict

n = int(input())

start = input()

g = defaultdict(lambda : [])

for _ in range(n):
    u, v = input().split()
    g[u].append(v)
    g[v].append(u)

s = [start]
vis = set([start])
while s:
    u = s.pop()
    for v in g[u]:
        if v not in vis:
            vis.add(v)
            s.append(v)

odd = 0
for k in g:
    odd += len(g[k]) % 2
    
print("ok" if len(g) == len(vis) and odd == 0 else "impossible")