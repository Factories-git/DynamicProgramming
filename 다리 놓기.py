import sys

input = sys.stdin.readline

t = int(input())
dp = [[0] * 30 for i in range(30)]
for i in range(1,30):
    dp[1][i] = i

for i in range(2,30):
    for j in range(i,30):
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

for _ in range(t):
    n,m = map(int, input().split())
    print(dp[n][m])