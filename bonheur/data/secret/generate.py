import random

for i in range(30):
    n = random.randint(1e4, 1e6)
    k = random.randint(1e7, 1e9)
    in_it = random.randrange(2)
    added = set()
    while len(added) != n:
        nb = random.randint(1, k-1)
        if in_it or  (k - nb not in added):
            added.add(nb)
    l = sorted(list(added))

    elements = set()
    ans = ""
    for el in l:
        if k - el in elements:
            ans = "yes"
            break
        elements.add(el)
    else:
        ans = ("no")
    with open(f"{i+3}_hidden.in", "w") as f:
        f.write(f"{n} {k}\n")
        f.write(" ".join(map(str, l))+"\n")
    
    with open(f"{i+3}_hidden.ans", "w") as f:
        f.write(ans+"\n")
