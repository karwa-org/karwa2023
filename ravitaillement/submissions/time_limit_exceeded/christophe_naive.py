n, m, k = list(map(int, input().split(' ')))
matrix, resp, max_area = [input().split(' ') for _ in range(n)], {input() for _ in range(k)}, 0
for i in range(n):
    for j in range(m):
        matrix[i][j] = matrix[i][j] in resp
for top in range(n):
    for left in range(m):
        for bottom in range(top, n):
            for right in range(left, m):
                if all(matrix[row][col] for row in range(top, bottom+1) for col in range(left, right+1)):
                    area = (bottom-top+1)*(right-left+1)
                    max_area = max(max_area, area)
print(max_area)