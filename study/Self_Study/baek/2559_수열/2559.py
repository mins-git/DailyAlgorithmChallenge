import sys
sys.stdin = open('input.txt')

"""
온도의 합이 가장 큰값을 알아보고자 함.
몇일동안의 온도 합이 가장 큰지 큰 값출력.
K 일만큼 더해가면됨.

"""


N,K = map(int, input().split()) # N 측정한 전체 날짜 수 #K는 연속적인 날짜 수
ondo = list(map(int,input().split()))


answer = sum(ondo[:K])  # K만큼만 자르고, 초기값 설정
current_sum = answer # 현재합으로 뒤에값을 구하면되잖아?

for i in range(1, N-K+1):
    current_sum = current_sum - ondo[i-1] + ondo[i+K-1] # 이전값을 빼고 다음값을 더하려는걸 하려는것임. 그러면 한칸씩 옮겨지잖아?
    if current_sum > answer :
        answer = current_sum

print(answer)


# ---------------------
# 시간초과
# for i in range(N-K): # 전체 온도 k만큼 더해봐야됨.
#     ondo_sum = 0
#     for j in range(K): # 연속 K일 진행 함.
#         ondo_sum += ondo[i+j]
#     if ondo_sum > answer:
#         answer = ondo_sum
#
# print(answer)