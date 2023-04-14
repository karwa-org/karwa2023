# TLE expected

import heapq


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
q = [(0, *start)]

dst = [[float("inf")]*w for _ in range(h)]
dst[start[0]][start[1]] = 0

while q:
    d, x, y = heapq.heappop(q)
    if d > dst[x][y]:
        continue
    if grid[x][y] == "B":
        break
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        xx = x + dx
        yy = y + dy
        if 0 <= xx < h and 0 <= yy < w and grid[xx][yy] != "#" and  dst[xx][yy] > dst[x][y] + 1:
            dst[xx][yy] = dst[x][y] + 1
            heapq.heappush(q, (dst[x][y]+1, xx, yy))

print("yes" if dst[end[0]][end[1]] != float("inf") else "no")
