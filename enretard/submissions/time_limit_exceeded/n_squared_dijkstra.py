# TLE expected


n,m = map(int, input().split())

g = [[] for _ in range(n)]

for _ in range(m):
    u,v,w = map(int, input().split())
    
    g[u-1].append((v-1, w))
    g[v-1].append((u-1, w))

dst = [float("inf")]*n
dst[0] = 0
q = set([(0,0)])

while q:
    el = min(q)
    q.remove(el)
    d, u = el 
    if u == n - 1:
        break
    if d > dst[u]:
        continue
    for v, w in g[u]:
        if dst[v] > w + d:
            dst[v] = w + d
            q.add((dst[v], v))
print(dst[n-1])