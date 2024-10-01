import sys

input = sys.stdin.readline

def func(i):
    global count
    if i > n:
        return
    if i == n:
        count += 1
        return
    for j in range(1,4):
        func(i + j)

t = int(input())
for _ in range(t):
    count = 0
    n = int(input())
    func(0)
    print(count)