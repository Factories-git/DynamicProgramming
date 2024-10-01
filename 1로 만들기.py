n = int(input())
arr = [0 for i in range(n+1)]
try:
    arr[2] = arr[3] = 1
except IndexError:
    pass
for i in range(4,n+1):
    arr[i] = arr[i-1] +1
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i//2]+1)
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i//3]+1)
if n == 1:
    print(0)
elif n == 2 or n == 3:
    print(1)
else:
    print(arr[n])
print(arr)