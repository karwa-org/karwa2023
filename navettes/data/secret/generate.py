import random
for i in range(20):
    n = random.randint(1e4, 1e9)
    m = random.randint(100, 1e9)
    with open(f"{i+2}_hidden.in", "w") as f:
        f.write(f"{n} {m}\n")
    with open(f"{i+2}_hidden.ans", "w") as f:
        f.write(str(n // m + (1 if n % m else 0))+"\n")

for i in range(50):
    n = random.randint(1e4, 1e9)
    m = (i + 1)*2
    with open(f"{i+2+20}_hidden.in", "w") as f:
        f.write(f"{n} {m}\n")
    with open(f"{i+2+20}_hidden.ans", "w") as f:
        f.write(str(n // m + (1 if n % m else 0))+"\n")