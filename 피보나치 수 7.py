n = int(input())
arr = [1 for i in range(n)]
arr.insert(0,0)
for i in range(2,n+1):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[-1] % 1000000007)