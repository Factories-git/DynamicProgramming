n = int(input())
arr = [1 for i in range(n)]
for i in range(2, n):
    arr[i] = arr[i - 1] + arr[i - 2]
print(arr[-1],n-2)
