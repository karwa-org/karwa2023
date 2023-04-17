n = int(input())

t = map(int, input().split())

def smallest_div(x):
    for i in range(2, x+1):
        if x % i == 0:
            return i

tab = [(smallest_div(x), x) for x in t]
tab = sorted(tab)
print(" ".join(map(lambda x: str(x[1]), tab)))
