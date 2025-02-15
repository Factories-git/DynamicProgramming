import sys

input = sys.stdin.readline

n = int(input())
d = [0] * (n + 2)
t = [0] * (n + 1)
p = [0] * (n + 1)

for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())

for i in range(n, -1, -1):
    if i + t[i] > n + 1:
        d[i] = d[i+1]
    else:
        d[i] = max(d[i+1], d[i+t[i]] + p[i])

print(d[1])