import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    dp = [0] * (m+1)
    dp[0] = 1
    for coin in arr:
        for j in range(coin, m+1):
            dp[j] += dp[j-coin]
    print(dp[m])