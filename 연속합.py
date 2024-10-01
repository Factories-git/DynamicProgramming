n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
answer = dp[0] = arr[0]

for i in range(1,n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])
    answer = max(dp[i], answer)
print(answer)