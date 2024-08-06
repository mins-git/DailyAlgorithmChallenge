import sys

sys.stdin = open('input.txt')


def erase(A):
    a = len(A)

    if a <= 3 :
        for i in range(a-1):
            if str_list[i] == str_list[i+1]:
                del str_list[i]
                del str_list[i]
                return str_list
    else:
        for i in range(a-2):
            # 만약 같은 문자가 있으면
            if str_list[i] == str_list[i+1]:
                del str_list[i]
                del str_list[i]
                return erase(str_list)
            else: str_list
        return str_list

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    A = input().strip()
    str_list = list(A)
    print(f'#{tc} {len(erase(str_list))}')


