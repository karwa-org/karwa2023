import random
import heapq


for it in range(20):
    n = random.randint(1e3, 1e4*5)
    m = int(1e5)
    max_w = int(1e6)
    append = set()
    edges = []
    mappings = [i+1 for i in range(n)]
    random.shuffle(mappings)

    for i in range(n-1):
        w = random.randint(1, max_w)
        edges.append((mappings[i], mappings[i+1], w))
        append.add((i, i+1))
        append.add((i+1, i))
    for _ in range(m - n + 1):
        w = random.randint(1, max_w)
        x = random.randrange(n)
        y = random.randrange(n)
        while x == y or (x,y) in append:
            x = random.randrange(n)
            y = random.randrange(n)
        append.add((x,y))
        append.add((y,x))
        edges.append((mappings[x], mappings[y], w))
    name = f"{it+3}_huge"
    with open(f"{name}.in", "w") as f:
        f.write(f"{n} {m}\n")
        f.write("\n".join(map(lambda t : f"{t[0]} {t[1]} {t[2]}", edges)))
        f.write("\n")