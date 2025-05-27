n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for i in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if dp[i][j] != 0 or i == j == 0:
            if i == j == n-1:
                break
            if i+board[i][j] < n:
                dp[i+board[i][j]][j] += dp[i][j]
            if j + board[i][j] < n:
                dp[i][j+board[i][j]] += dp[i][j]
for i in dp:
    print(i)