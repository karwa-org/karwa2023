for h in range(__import__('math').floor(2**.5*int(input())), -1, -1):# edge case if we include h=ceil(2**.5*n) when h is palindromic
    if str(h) == str(h)[::-1]:
        print(h*h4)
        break