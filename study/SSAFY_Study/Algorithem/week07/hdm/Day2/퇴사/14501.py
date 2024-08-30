import sys
sys.stdin = open('input.txt')

"""
상담원으로 일하는 백준이 퇴사
오늘부터 N + 1 일째 되는 날 퇴사하려함.
남은 N일동안 최대한 많은 상담하려함.

상담 후 최대수익 구하시오.
최대 15일

3 / 10 = 해당 일할계산값.
5 / 20 일 = 4
첫 일자가 다 될 때까지 
"""
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 메모이제이션 준비
dp = [0] * (N+1)

for idx, price in enumerate(arr):

