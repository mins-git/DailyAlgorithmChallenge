import sys
sys.stdin = open('input.txt')

"""
그림과 같이 각각의 계단에 점수 얻음
1. 1계단 or 2계단 가능
2. 연속 3번 밟기x
3 마지막 반드시 밟아

"""

stair_count = int(input())

# 메모이제이션 준비
stair = [0] * (stair_count+1) #[0, 10, 20, 15, 25, 10, 20]
dp = [0] * (stair_count+1)

# dp[4] = max(dp[3] + dp[4], dp[2] + dp[4])
# 2의 배수는 직전칸을 밟았으면 아돼

for i in range(1, stair_count+1):
    stair[i] = int(input())

dp[1] = stair[1]
dp[2] = stair[2]
dp[3] = max(dp[1] + dp[3], dp[2] + dp[3])

for i in range(4, stair_count+1):
    dp[i] = max(dp[i-1] + stair[i], dp[i-2] + stair[i])
    # print(i, dp[i])

print((dp[stair_count]))
