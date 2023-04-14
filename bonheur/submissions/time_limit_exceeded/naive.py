# TLE expected

n, k = map(int, input().split())
a = list(map(int, input().split()))


for i in range(n):
    for j in range(i+1, n):
        if a[i] + a[j] == k:
            print("yes")
            exit()

print("no")