m = int(input())

arr = [2,5]

d = [100001] * (m + 1)

d[0] = 0

for i in range(2):
    for j in range(arr[i], m + 1):
        if d[j - arr[i]] != 10001:
            d[j] = min(d[j], d[j - arr[i]] + 1)

print(d[m] if d[m] != 100001 else -1)