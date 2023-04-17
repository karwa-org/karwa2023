class UnionFind:
    def __init__(self):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xRoot, yRoot = self.find(x), self.find(y)
        if xRoot != yRoot:
            if self.rank[xRoot] < self.rank[yRoot]:
                self.parent[yRoot] = xRoot
            else:
                self.parent[xRoot] = yRoot
                if self.rank[xRoot] == self.rank[yRoot]:
                    self.rank[xRoot] += 1

n, m = list(map(int,input().split()))
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u-1,v-1,w))#bisect.insort(edges, (u-1,v-1,w), key=lambda v:v[2])
edges.sort(key=lambda v: v[2])

def kruskal(bound):
    cost, count = 0, 0
    uf = UnionFind()
    for u,v,w in edges:
        if w >= bound and uf.find(u) != uf.find(v):
            count += 1
            cost += w
            uf.union(u,v)
    if count == n-1:
        return cost
    else:
        return float('+inf')

lowest, low, high = kruskal(0), 0, edges[-1][2] + 1
while high > low:
    mid = (high + low) // 2
    if kruskal(mid) <= int(lowest*1.25):
        low = mid + 1
    else:
        high = mid
print(low-1)