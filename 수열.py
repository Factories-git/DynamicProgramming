n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
for i in range(1, n):
    for j in range(i):
        if arr[j] <= arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
maxes = max(dp)
print(dp)
dp = [0] * n
for i in range(1, n):
    for j in range(i):
        if arr[j] >= arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(max(dp), maxes))
print(dp)