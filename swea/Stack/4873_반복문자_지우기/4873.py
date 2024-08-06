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


#  스택 활용하면 더 쉬움.
# for tc in range(1,T+1):
#   word = list(map(str, input()))
#   stack = []
#   stack.append(word[0])  #첫번째 값을 stack에 추가시켜주고
#
#   for i in range(1,len(word)):  # i번 반복하되, word만큼 반복할것임
#     if not stack: # 만약에 stack안에 값이 없으면
#       stack.append(word[i]) # 스택에 현재 값추가해주고
#     elif word[i] == stack[-1]: # 현재 i 값과, 스택의 제일 위의 값이 동일하다면
#       stack.pop() # 스택에 들어잇는값 제거해주고
#     else:
#       stack.append(word[i]) # 그외는 stack에 전부 추가해주면됨.
#
#   print(f'#{tc} {len(stack)}') # 스택길이 추가해주면 되겠지?

