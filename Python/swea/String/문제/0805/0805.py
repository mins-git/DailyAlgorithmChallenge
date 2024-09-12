import sys

sys.stdin = open('input.txt')


def is_palindrome(s):

    left, right = 0, len(s) -1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# Testcase 수
T = 2
# Testcase 만큼 반복
for tc in range(1, T+1):

    # 회문 3~8글자 회문 체크

    pal_len = int(input())
    arr = [input() for _ in range(8)]
    count = 0

    for i in range(8):
        for j in range(8 - pal_len + 1):
            ispal = arr[i][j:j+pal_len]
            if is_palindrome(ispal):
                count +=1

    arr_b = list(zip(*arr))

    for i in range(8):
        for j in range(8 - pal_len + 1):
            ispal = arr_b[i][j:j+pal_len]
            if is_palindrome(ispal):
                count +=1

    print(f'#{tc} {count}')


