def dfs(graph, u, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, v, visited)
n, start, graph = int(input()), input(), {}
graph[start] = []
for _ in range(n):
    a, b = input().split()
    if b not in graph: graph[b] = []
    if a not in graph: graph[a] = []
    graph[a].append(b)
visited = {v: False for v in graph}
dfs(graph, start, visited)
if any(not visited[v] for v in graph):
    print("impossible")
else:
    print("impossible" if any(len(graph[v]) % 2 != 0 for v in graph) else "ok")