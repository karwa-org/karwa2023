n, m, k = list(map(int, input().split(' ')))
matrix, resp, max_area = [input().split(' ') for _ in range(n)], {input() for _ in range(k)}, 0
for i in range(n):
    for j in range(m):
        matrix[i][j] = matrix[i][j] in resp
height, left, right = [0]*m, [0]*m, [m]*m
for i in range(n):
    for j in range(m):
        height[j] = height[j]+1 if matrix[i][j] else 0
    cur_left, cur_right = 0, m
    for j in range(m):
        left[j], cur_left = (max(left[j], cur_left), cur_left) if matrix[i][j] else (0, j+1)
    for j in range(m-1, -1, -1):
        right[j], cur_right = (min(right[j], cur_right), cur_right) if matrix[i][j] else (m, j)
    for j in range(m):
        max_area = max(max_area, height[j] * (right[j]-left[j]))
print(max_area)