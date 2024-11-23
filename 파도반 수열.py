import sys

input = sys.stdin.readline

dp = [0, 1, 1]
for i in range(3,101):
    dp.append(dp[i-3] + dp[i-2])
for i in range(int(input())):
    n = int(input())
    print(dp[n])