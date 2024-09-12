import sys

sys.stdin = open('input.txt')


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    # str로들어옴.
    N = input()
    M = input()

    M_len = len(M)
    N_len = len(N)
    result = 0

    if N_len > M_len :
        result = 0
        break

    for i in range(M_len):
        if M[i:i + N_len] == N:
            result = 1
            print(f'#{tc} {result}')
            break
    else:print(f'#{tc} {result}')