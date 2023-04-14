from collections import deque


h,w = map(int, input().split())

grid = [input() for _ in range(h)]
start = (0,0)
end = (0, 0)    
for i in range(h):
    for j in range(w):
        if grid[i][j] == "K":
            start = (i,j)
        elif grid[i][j] == "B":
            end = (i,j)
q = deque([start])

vis = [[False]*w for _ in range(h)]

while q:
    x, y = q.popleft()
    if vis[x][y]:
        continue
    vis[x][y] = True
    if grid[x][y] == "B":
        break
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        xx = x + dx
        yy = y + dy
        if 0 <= xx < h and 0 <= yy < w and grid[xx][yy] != "#" and not vis[xx][yy]:
            q.append((xx,yy))

print("yes" if vis[end[0]][end[1]] else "no")
