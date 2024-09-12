import sys

sys.stdin = open('input.txt')


def banana(A, B):
    count = 0
    i = 0
    B_len = len(B)
    A_len = len(A)

    while i <= A_len - B_len:
        if A[i:i + B_len] == B:
            count += 1
            i += B_len
        else:
            i += 1
            count += 1

    count += (A_len - i)
    return count

    # if B in A:
    #     for char in range(A_len - B_len + 1):
    #         if A[char: char + B_len] == B:
    #             count -= B_len
    #             count += 1
    #     return count
    # else:
    #     return A_len


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    A, B = map(str, input().split())

    result = banana(A, B)
    print(f'#{tc} {result}')





