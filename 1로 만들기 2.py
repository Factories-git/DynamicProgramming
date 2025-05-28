n = int(input())
dp = [0] * (10**6 + 1)
dp[2] = dp[3] = 1
path = [n]

for i in range(4, n+1):
    dp[i] = dp[i-1] + 1
    w = 0
    if i % 2 == 0:
        w = 2
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        w = 3
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])
c = 0
while True:
    s = path[-1]
    if s == 1:
        break
    if s % 2 == 0 and s % 3 == 0:
        if dp[s-1] < dp[s//2] and dp[s-1] < dp[s//3]:
            s -= 1
        elif dp[s-1] > dp[s//2] and dp[s//2] < dp[s//3]:
            s //= 2
        else:
            s //= 3
    else:
        if s % 2 == 0:
            if dp[s-1] < dp[s//2]:
                s -= 1
            else:
                s //= 2
        elif s % 3 == 0:
            if dp[s-1] < dp[s//3]:
                s -= 1
            else:
                s //= 3
        else:
            s -= 1
    path.append(s)
print(*path)