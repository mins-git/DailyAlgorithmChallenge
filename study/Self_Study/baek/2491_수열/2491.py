import sys
import itertools
sys.stdin = open('input.txt')

"""
연속해서 커지거나(같거나) 연속해서 작아지거나(같거나)
가장 긴 길이 측정

"""

# itertools.combinations()
# itertools.permutations()
# itertools.combinations_with_replacement()


N = int(input())
#수열
arr = list(map(int, input().split())) #[1, 2, 2, 4, 4, 5, 7, 7, 2]

min_result = 1
min_max = 1
max_result = 1
max_max = 1


# 작아지는것 표현
for i in range(1, N):
    if arr[i] >= arr[i-1]:
        min_result +=1

        # 사이즈가 달라지면
    else:
        min_max = max(min_result,min_max)
        min_result = 1

max_up = max(min_result,min_max)

# 뒤에게 더 크면?
for i in range(1, N):
    if arr[i] <= arr[i-1]:
        max_result +=1

    # 만약 앞뒤 값이 다르면?
    else:
        max_max = max(max_result, max_max)
        max_result = 1



max_down = max(max_max, max_result)

print(max(max_down,max_up))

#
# def check(max_max,min_max):
#
#     if max_max <= max_result:
#         max_max = max_result
#         # return max_result+1
#
#     if max_max > max_result:
#         return 2
#
#     if min_max <= min_result :
#         min_max = min_result
#         # return min_result
#
#     if min_max > min_result :
#         return 2
#
#     return max(max_result+1, min_result, 2)
#
# print(check(max_max, min_max))