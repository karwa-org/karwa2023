graph = {}
visited = set()

def dfs(node, edges_left, start):
    visited.add(node)
    if edges_left == 0 and node == start:
        return True
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor, edges_left - 1, start):
                return True
    visited.remove(node)
    return False

def dfs2(graph, u, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs2(graph, v, visited)

n = int(input())
start = input().strip()
for i in range(n):
    from_, to = input().strip().split()
    if from_ not in graph:
        graph[from_] = []
    if to not in graph:
        graph[to] = []
    graph[from_].append(to)
    graph[to].append(from_)

edges_left = sum(len(neighbors) for neighbors in graph.values()) // 2
_ = dfs(start, edges_left, start)


visited2 = {v: False for v in graph}
dfs2(graph, start, visited2)
if any(not visited2[v] for v in graph):
    print("impossible")
else:
    print("impossible" if any(len(graph[v]) % 2 != 0 for v in graph) else "ok")
