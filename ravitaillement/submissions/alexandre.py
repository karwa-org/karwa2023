# from https://cp-algorithms.com/dynamic_programming/zero_matrix.html

n, m, k = map(int, input().split())

mat = []
for _ in range(n):
    mat.append(input().split())

resp = set()
for _ in range(k):
    resp.add(input())

ans = 0
d = [-1]*m
d1 = [0]*m
d2 = [0]*m
for i in range(n):
    st = []
    for j in range(m):
        if mat[i][j] not in resp:
            d[j] = i
    for j in range(m):
        while st and d[st[-1]] <= d[j]:
            st.pop()
        d1[j] = -1 if not st else st[-1]
        st.append(j)
    st.clear()
    for j in range(m - 1, -1, -1):
        while st and d[st[-1]] <= d[j]:
            st.pop()
        d2[j] = m if not len(st) else st[-1]
        st.append(j)
    st.clear()
    for j in range(m):
        ans = max(ans, (i - d[j])*(d2[j]-d1[j]-1))
print(ans)