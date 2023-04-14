import random

for i in range(30):
    n = random.randint(int(1e7), int(1e8))
    if random.randrange(2):
        k = random.randint(100, n - 1)
    else:
        k = random.randint(100, n-1)
        n += k + 1 - n % (k+1)


    ans = ("Brieuc" if n % (k + 1) else "Aymeric")
    with open(f"{i+2}_hidden.in", "w") as f:
        f.write(f"{n} {k}\n")
    with open(f"{i+2}_hidden.ans", "w") as f:
        f.write(ans)
        f.write("\n")

