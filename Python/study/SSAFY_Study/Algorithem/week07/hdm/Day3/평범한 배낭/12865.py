import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())  # 물건수 N / 무게 K
arr = [list(map(int, input().split())) for _ in range(N)]  # [[1, 10], [7, 10], [3, 1], [5, 0]]
dp = [0] * (K + 1) # 무게별 최대 가치 기록

for i in range(N):
    weight, value = arr[i]  # 무게와 가치를 뽑아낸 후

    if value == 0:
        continue

    for j in range(K, weight -1, -1):
        dp[j] = max(dp[j], dp[j-weight] + value)

print(max(dp))

"""
N개의 물건
무게 W / 가치 v
k만큼 넣을 수 있음.
무게 K넘지말기.

N만큼 회전하면서, 

dp 에 최대 가치를 저장하기. 

1. dp[1] 만약 k보다 w가 작으면 넣을 수 있음. K 
     - if K > W : dp[1] = K

2. dp[2]는 1이랑 2랑 비교해봐야됨. 3가지겠지?
     1. dp[1]이 더클 경우
     2. 2번째 k값이 더 크면서 w로 담을 수 있는 경우 ( w초과시 ) 하나만 담는 경우
     3. 둘다 담는 경우 w두개 더한값이 k보다 작아서 둘다 담을경우

3. dp[3]은
        if K <= w
    1. dp 1만 담거나 dp2만 담거나 dp3만담거나 (혼자 담는경우)
        if K <= w : 최대 무게 이내면
        v가치가 가장 높은 것 다담아야지.

        # 현재 계산한 최대값은 새롭게 구해야됨.
        max(dp[i-1], .) #직전까지의 최대값과

    # 현재 계산한 최대값 어떻게 구하게?

    버틸 수 있는 무게 K이내의 조합을 구해봐야지 그중 최대 V를 찾으면됨.
    버틸 수 있는 무게 k이내의 조합은 어떻게 구해?

    dp는 최소단위로 나눠서 계산을 덜 하는 방식임.


    2. dp 1, dp2 만담거나 dp1,3 dp 2,3 (둘씩 담거나)
    3. 모두 다 담거나
풀이:
"""




"""
N , K = map(int, input().split()) # 물건수 N / 무게 K
arr = [list(map(int, input().split())) for _ in range(N)] # [[6, 13], [4, 8], [3, 6], [5, 12]]

dp_result = [0] * (N+1)
arr.sort(key = lambda x: (-x[1], x[0])) #[[6, 13], [5, 12], [4, 8], [3, 6]]
                                        #[[1, 10], [7, 10], [4, 1], [2, 0]]

print(arr)
for j in range(N): # 앞에서부터 차례로 순회.
    recent_weight = 0
    dp = [0] * (N+1)
    for i in range(j,N):
        weight, value = arr[i] # 무게와 가치를 뽑아낸 후
        if value == 0:
            continue
        # i에 이미담은 무게의 합이 들어와야함.
        if recent_weight + weight <= K: # 만약 가방에 물건을 담았다라면,
            dp[i] = max(dp[i-1], dp[i-1] + value)
            if dp_result[i] < dp[i]:
                dp_result[i] = sum(dp)
            recent_weight += weight

        # 가방에 물건을 담지 않았으면,
        else:
            dp[i+1] = max(dp[i], dp[i+1])
            if dp_result[i+1] < dp[i+1]:
                dp_result[i+1] = dp[i+1]

print(max(dp_result))
"""