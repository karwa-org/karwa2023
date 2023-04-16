import heapq
from collections import defaultdict
n, m = list(map(int,input().split()))
adj = defaultdict(list)
for _ in range(m):
    u, v, w = list(map(int,input().split()))
    adj[u-1].append([v-1,w])
    adj[v-1].append([u-1,w])
def dijkstra(s):
    dist = [1e18 for _ in range(n)]
    dist[s], q = 0, [(0,s)]
    while q:
        cur_dist, u = heapq.heappop(q)
        if dist[u] < cur_dist: continue
        for v in adj[u]:
            v[1] += cur_dist
            if dist[v[0]] > v[1]:
                dist[v[0]] = v[1]
                heapq.heappush(q,(v[1],v[0]))
    return dist
print(dijkstra(0)[n-1])