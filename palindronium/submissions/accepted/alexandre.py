n = int(input())

for h in range(int(2**0.5*n), -1, -1):
    if str(h) == str(h)[::-1]:
        print(h**2/4)
        break