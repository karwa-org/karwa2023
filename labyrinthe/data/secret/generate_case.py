import random
from collections import deque

for i in range(30):
    h = int(2000)
    w = random.randint(1500, 2000)

    grid = [["." if random.randint(1,5) % 2 else "#" for _ in range(w)] for _ in range(h)]
    start = (random.randrange(h), random.randrange(w))
    end = (random.randrange(h), random.randrange(w))
    while end == start:
        end = (random.randrange(h), random.randrange(w))
    grid[start[0]][start[1]] = "K"
    grid[end[0]][end[1]] = "B"

    vis = [[False]*w for _ in range(h)]
    q = deque([start])
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

    res = "yes" if vis[end[0]][end[1]] else "no"
    with open(f"{i+3}_huge.in", 'w') as f:
        f.write(f"{h} {w}\n")
        f.write("\n".join("".join(grid[i]) for i in range(h))+"\n")
    with open(f"{i+3}_huge.ans", "w") as f:
        f.write(res)
        f.write("\n")