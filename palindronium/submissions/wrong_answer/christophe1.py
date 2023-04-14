for h in range(round(2**.5*int(input()))):
    if str(h) == str(h)[::-1]:
        print(h*h/4)
        break