import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n + 1)] #dp 배열 초기화
item = [[0, 0] for _ in range(n + 1)] # 무게, 가치 순으로 저장

for i in range(1, n+1):
    item[i][0], item[i][1] = map(int, input().split()) # 무게, 가치 순으로 저장

for i in range(1, n+1):
    for w in range(1, k+1):
        if item[i][0] <= w: #만약 넣을 수 있다면
            if item[i][1] + dp[i-1][w-item[i][0]] > dp[i-1][w]: #현재 가치 + 이 물건을 넣지 않았을때의 가치가 이전 가치보다 크면
                dp[i][w] = item[i][1] + dp[i-1][w-item[i][0]] #갱신
            else: #넣지 않았을때의 가치가 더 크다면
                dp[i][w] = dp[i-1][w] #그냥 갱신 안 함
        else: # 넣을 수 없다면
            dp[i][w] = dp[i-1][w] # 갱신은 안함

print(dp[n][k]) #출력