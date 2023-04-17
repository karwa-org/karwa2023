n = int(input())

import math
h = math.floor(math.sqrt(2) * n)

def is_palindrome(h):
    return str(h) == str(h)[::-1]

while(not is_palindrome(h)): 
    h-=1
print(h**2 / 4)
