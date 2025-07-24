import sys

input = sys.stdin.readline

n = int(input())
sequence = input().split()
dp = [[0] * n for _ in range(n)]
for i in range(n): # 1글자는 팰린드롬 취급
    dp[i][i] = 1

for i in range(n-1): # 2글자가 같은 경우도 팰린드롬 취급
    if sequence[i] == sequence[i+1]:
        dp[i][i+1] = 1

for length in range(3, n+1): # 만들 수 있는 팰린드롬 길이에 대해 반복(2개 까지는 이미 만들었으니 3개 부터 n개 까지 반복)
    for i in range(n - length + 1): # n - length + 1 하는 이유 -> 뭐가됐든 i ~ j까지 length 길이의 팰린드롬 확인할거
        j = i + length - 1 #j도 정함
        if sequence[i] == sequence[j] and dp[i+1][j-1] == 1: #새로 추가되는 수 둘이 같니? 그리고 dp[i+1][j-1](중간에 있는애)가 팰린드롬이니?
            dp[i][j] = 1 #그러면 얘도 팰린드롬입니다

for i in range(int(input())):
    s, e = map(int, input().split()) #질의 처리
    print(dp[s-1][e-1])