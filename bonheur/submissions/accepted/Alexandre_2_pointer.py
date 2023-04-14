n, k = map(int, input().split())

a = list(map(int, input().split()))

# a alreay sorted
# sorted(a)

i = 0
j = n - 1

while j > i:
    if a[i] + a[j] == k:
        print("yes")
        break
    elif a[i] + a[j] > k:
        j -= 1
    else:
        i += 1
else:
    print("no")