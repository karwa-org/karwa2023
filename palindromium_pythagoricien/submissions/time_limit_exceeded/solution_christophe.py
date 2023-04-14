import math
maxi = -1
for h in range(math.ceil(2**.5*int(input()))):
    curr = h*h/4
    if str(h) == str(h)[::-1]:
        maxi = max(maxi, curr)
print(maxi)