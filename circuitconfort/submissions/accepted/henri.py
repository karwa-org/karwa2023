import sys
sys.setrecursionlimit(1001)

n = int(input())
starting_station = input().strip("\n")

adj = {starting_station: []}
visited = {starting_station: False}

for i in range(n):
    a, b = input().strip("\n").split()
    if a not in adj:
        adj[a] = []
        visited[a] = False
    if b not in adj:
        adj[b] = []
        visited[b] = False
    adj[a].append(b)
    adj[b].append(a)


def dfs(x):
    if visited[x]: return
    visited[x] = True
    for y in adj[x]:
        dfs(y)

dfs(starting_station)

fail = False
for x in adj:
    if len(adj[x]) % 2 == 1:
        fail = True

if fail or sum([1 for x in visited if visited[x]]) != len(adj):
    print("impossible")
else:
    print("ok")

