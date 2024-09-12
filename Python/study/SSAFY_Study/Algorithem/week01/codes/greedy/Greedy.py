# 주어진수 M번 더하여 가장 큰수 만들기.
# 단, K번을 초과하여 더해질 수 없음.
# 인덱스가 다르면 다른값이라고 봄.

# 첫줄에 N, M , K 주어짐. 

import sys

sys.stdin = open('input.txt')

N, M, K = list(map(int,input().split()))   # 테스트 케이스 N / 주어진 M / K번 진행
numbers = list(map(int, input().split()))  # n개의 자연수
sort_numbers = sorted(numbers, reverse=True)
result = 0
count = 0
print(sort_numbers)
# K번만 진행가능. M개까지만 

for i in range(M):
    if count > 1:
    # N개의 자연수중 sort진행.
        for j in range(K):
            if count > 1:
                result += sort_numbers[j]
                count += 1
                return result
            else : print(result)
    else: print(result)