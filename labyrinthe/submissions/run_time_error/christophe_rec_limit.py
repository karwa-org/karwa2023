def dfs(i, j):
    visited[(i,j)] = True
    for v in {(i-1,j) if i>0 else -1,(i+1,j) if i<n-1 else -1,(i,j-1) if j>0 else -1, (i,j+1) if j<m-1 else -1}:
        if v != -1 and city[v[0]][v[1]] != '#' and not visited[v]:
            dfs(*v)
n,m = list(map(int,input().split()))
city,visited = [list(input()) for _ in range(n)], __import__("collections").defaultdict(lambda: False)
for i in range(n):
    for j in range(m):
        if city[i][j] == "B": dest = (i,j)
        elif city[i][j] == "K": start = (i,j)
dfs(*start)
print("yes" if visited[dest] else "no")
