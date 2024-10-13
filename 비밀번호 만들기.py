'''
LCS 문제랑 원래는 같았으나 ChatGPT에게 물어봐 작성된 코드

'''
import sys

input = sys.stdin.readline
A = list(input().strip())
B = list(input().strip())

# DP 테이블 생성
dp = [[0 for _ in range(len(B) + 1)] for i in range(len(A) + 1)]

# LCS 길이 계산
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# LCS 역추적 함수 (Bottom-up 방식)
def getLCS():
    r, c = len(A), len(B)
    LCS = []

    while r > 0 and c > 0:
        if A[r - 1] == B[c - 1]:  # 문자가 같으면 대각선 위로 이동
            LCS.append(A[r - 1])
            r -= 1
            c -= 1
        elif dp[r - 1][c] >= dp[r][c - 1]:  # 위쪽이 더 크면 위로 이동
            r -= 1
        else:  # 왼쪽이 더 크면 왼쪽으로 이동
            c -= 1

    return ''.join(reversed(LCS))  # 역순으로 저장했으므로 뒤집어 출력

# 결과 출력
print(getLCS())
