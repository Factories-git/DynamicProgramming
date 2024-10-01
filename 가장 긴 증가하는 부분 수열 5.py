import sys, time

input = sys.stdin.readline
start = time.time()
n = int(input())
A = list(map(int, input().split()))
A.insert(0,0)
idx = 0
max_l = 1
b = [0] * 1000001
b[1] = A[1]
d = [0] * 1000001
d[1] = 1
ans = [0] * 1000001


def binarysearch(l, r, now):
    while l < r:
        mid = (l + r) // 2
        if b[mid] < now:
            l = mid + 1
        else:
            r = mid
    return l


for i in range(2, n + 1):
    if b[max_l] < A[i]:
        max_l += 1
        b[max_l] = A[i]
        d[i] = max_l
    else:
        idx = binarysearch(1, max_l, A[i])
        b[idx] = A[i]
        d[i] = idx
print(max_l)
idx = max_l
x = b[max_l] + 1

for i in range(n, 0, -1):
    if d[i] == idx:
        ans[idx] = A[i]
        idx -= 1

for i in range(1, max_l + 1):
    print(ans[i], end=' ')
