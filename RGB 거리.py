n = int(input())
RGB = []
dp = [''] * n
for i in range(n):
    RGB.append(list(map(int, input().split())))
for i in range(n):
    se = set(RGB[i])
    m = min(RGB[i])
    s = RGB[i].index(m)
