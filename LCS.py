import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)
A = list(input().strip())
B = list(input().strip())
dp = [[0 for _ in range(len(B) + 1)] for i in range(len(A) + 1)]
Path = []

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(A)][len(B)])


def getText(r, c):
    if r == 0 or c == 0:
        return
    if A[r - 1] == B[c - 1]:
        Path.append(A[r - 1])
        getText(r - 1, c)
    else:
        if dp[r - 1][c] > dp[r][c - 1]:
            getText(r - 1, c)
        else:
            getText(r, c - 1)


getText(len(A), len(B))

print(''.join(reversed(Path)))
