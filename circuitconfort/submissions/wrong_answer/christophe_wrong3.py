def dfs(graph, u, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, v, visited)
n, start, graph = int(input()), input(), __import__("collections").defaultdict(list)
for _ in range(n):
    a, b = input().split()
    graph[a].append(b)
    graph[b].append(a)
visited = {v: False for v in graph}
dfs(graph, a, visited)
if any(not visited[v] for v in graph):
    print("impossible")
else:
    print("impossible" if any(len(graph[v]) % 2 != 0 for v in graph) else "ok")