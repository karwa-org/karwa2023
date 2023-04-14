for h in range(round(2**.5*int(input())), -1, -1):# edge case if we include h=ceil(2**.5*n) when h is palindromic
    if str(h) == str(h)[::-1]:
        print(h*h/4)
        break