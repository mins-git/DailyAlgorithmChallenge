import sys

sys.stdin = open('input.txt')


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum = 0

    for r in range(N):
        for c in range(N):
            if r == c :
                sum += arr[r][c]
            elif N - r -1 == c:
                sum += arr[r][c]

    print(sum)