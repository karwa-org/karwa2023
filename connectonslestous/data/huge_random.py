import random
n = int(100000)
m = int(2*100000)

mappings = [i+1 for i in range(n)]
random.shuffle(mappings)
lst = []

tot = 0
added = set()
for i in range(n-1):
    w = random.randint(1, int(1e9))
    lst.append((mappings[i], mappings[i+1], w))
    tot += w
for i in range(m-n+1):
    
    start = random.randint(1, n)
    end = random.randint(1, n)
    w = random.randint(1, int(1e9))
    while start == end or (start, end) in added:
        start = random.randint(1, n)
        end = random.randint(1, n)
    lst.append((mappings[start-1], mappings[end-1], w))
    added.add((start,end))
    added.add((end, start))
    tot += w


name = "17_huge"
with open(f"{name}.in", "w") as f:
    f.write(f"{n} {m}\n")
    f.write("\n".join(map(lambda t : f"{t[0]} {t[1]} {t[2]}", lst)))
