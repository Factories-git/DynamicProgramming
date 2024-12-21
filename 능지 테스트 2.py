dp = [100] * 10
price = [12, 21, 31, 40, 49, 58, 69, 79, 90, 101]

for i in range(10):
    for j in range(1,11):
        if i-j >= 0:
            dp[i] = dp[i-j]+price[j]
print(dp[4]*1000)