n = int(input())
dp = [1,1]
while len(dp) < n:
    dp.append(dp[-1]+dp[-2])
print(dp[-1])