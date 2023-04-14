n,m = map(int, input().split())

edges = []
mx = 0
for i in range(m):
    u,v,w = map(int, input().split())
    edges.append((u-1,v-1,w))
    mx = max(mx, w)

edges.sort(key=lambda x: x[2])

parents = [i for i in range(n)]
rank = [0]*n
def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if rank[x] > rank[y]:
            parents[x] = y
        elif rank[y] > rank[x]:
            parents[y] = x
        else:
            parents[x] = y
            rank[x] += 1

def kruskal(alpha):
    for i in range(n):
        rank[i] = 0
        parents[i] = i
    ans = 0
    comp = 0
    for u,v,w in edges:
        if w >= alpha and find(u) != find(v):
            ans += w
            union(u, v)
            comp += 1
    return ans if comp + 1 == n else float('inf')

best = (kruskal(0))
lo = 0
hi = mx + 1

while hi > lo:
    mid = lo + (hi - lo) // 2
    res = kruskal(mid)
    if res <= int(best*1.25):
        lo = mid + 1
    else:
        hi = mid
print(lo - 1)

