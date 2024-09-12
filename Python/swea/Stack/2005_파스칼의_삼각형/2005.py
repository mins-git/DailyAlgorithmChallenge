import sys

sys.stdin = open('input.txt')


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    arr = [[0] * N for _ in range(N)]
    print(f'#{tc}')

    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i: # 각 행의 첫번째 요소 0과 마지막 요소 i는 1
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            print(arr[i][j], end=' ')
        print()

    # N인 파스칼의 삼각형을 만들어야함.
    # 첫줄 1
    # 두번재줄 ~ 각 숫자들은 오른쪽 왼쪽 합이랑 같음
    # 본인의 인덱스 + 직전인덱스 더하기





# 2차풀이
# def permutation(n):
#     permutation = []
#     for i in range(n + 1):
#         if i == 0:
#             permutation.append(1)
#         else:
#             numerator = 1
#             denominator = 1
#             for j in range(i):
#                 numerator *= (n - j)
#                 denominator *= j + 1
#             permutation.append(numerator // denominator)
#
#     return permutation
#
#
# for tc in range(1, T + 1):
#     n = int(input())
#     print(f'#{tc}')
#     for i in range(n):
#         print(*permutation(i))
