"""
인접한 집들과 방범 장치가 연결되어있음
인접한 두 집을 털면 경보 울림
도둑이 훔칠돈의 최대값?

# 3집은 1집의 최대값
# 4집은 2집의 최대값
# 5집은 3집의 최대값
"""


def solution(money):

    dp = [0] * len(money)
    # 첫집을 무조건 털 경우.
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])

    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i - 1], money[i] + dp[i - 2])
    # 마지막집 털면 x
    a = max(dp)


    # 마지막집을 무조건 털 경우.
    sec_dp = [0] * len(money)
    sec_dp[0] = 0
    sec_dp[1] = money[1]

    for i in range(2, len(money) - 1):
        sec_dp[i] = max(sec_dp[i - 1], money[i] + sec_dp[i - 2])
    b = max(sec_dp)

    result = max(a, b)

    return result
