import sys

input = sys.stdin.readline

t = int(input())

arr = [[0 for i in range(41)] for j in range(2)]
arr[0][0] = arr[1][1] = 1

for i in range(2,41):
    arr[0][i] = arr[0][i-1] + arr[0][i-2]
    arr[1][i] = arr[1][i-1] + arr[1][i-2]

for i in range(t):
    n = int(input())
    print(arr[0][n], arr[1][n])