n, k = map(int, input().split())

a = list(map(int, input().split()))

elements = set()
for el in a:
    if k - el in elements:
        print("yes")
        break
    elements.add(el)
else:
    print("no")