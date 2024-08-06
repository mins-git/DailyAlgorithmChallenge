import sys

sys.stdin = open('input.txt')


def jisu(N, M, a):

    #result 를 선언
    global result
    # result에
    result = result * N
    a += 1

    if a < M:
        return jisu(N, M, a)

    else: return result

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):

    test_case = int(input())

    N, M = map(int, input().split())
    a = 0
    result = 1

    print(f'#{tc} {jisu(N, M, a)}')


