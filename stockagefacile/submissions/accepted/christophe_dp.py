MOD = 10**9 + 7

n = int(input())
if n <= 1:
    print(1)
else:
    dp = [[0, 0] for _ in range(n+1)]
    dp[1][0] = 1
    dp[1][1] = 1

    for i in range(2, n+1):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
        dp[i][1] = dp[i-1][0]

    print((dp[n-1][0] + dp[n-1][1]) % MOD)
