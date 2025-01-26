n = int(input())
s = [float(input()) for _ in range(n)]
dp = [0] * n
dp[0] = s[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] * s[i], s[i])

print('%.3f' % max(dp))

# 또 다른 방법(메모리 줄임)
n = int(input())
s = [float(input()) for _ in range(n)]
max_pro = s[0]
cur_pro = s[0]
for i in range(1, n):
    cur_pro = max(cur_pro * s[i], s[i])
    max_pro = max(max_pro, cur_pro)
print('%.3f' % max_pro)