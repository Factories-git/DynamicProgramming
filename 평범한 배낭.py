import sys

input = sys.stdin.readline
n,k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n + 1)]
item = [[0,0] for _ in range(n + 1)]

for i in range(1, n + 1):
    item[i][0], item[i][1] = map(int, input().split())

for i in range(1, n + 1):
    for w in range(1, k + 1):
        if item[i][0] <= w:
            if item[i][1] + dp[i-1][w-item[i][0]] > dp[i-1][w]:
                dp[i][w] = item[i][1] + dp[i-1][w-item[i][0]]
            else:
                dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = dp[i-1][w]

print(dp[n][k])