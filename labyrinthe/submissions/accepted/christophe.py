n,m = list(map(int,input().split()))
city,visited = [list(input()) for _ in range(n)], [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if city[i][j] == "B": dest = (i,j)
        elif city[i][j] == "K": start = (i,j)
queue, visited[start[0]][start[1]], u = [start], True, None
while queue:
    (i,j) = queue.pop()
    if (i,j) == dest: break
    for v in {(i-1,j) if i>0 else -1,(i+1,j) if i<n-1 else -1,(i,j-1) if j>0 else -1, (i,j+1) if j<m-1 else -1}:
        if v != -1 and city[v[0]][v[1]] != '#' and not visited[v[0]][v[1]]:
            visited[v[0]][v[1]] = True
            queue.append(v)
print('yes' if (i,j) == dest else 'no')