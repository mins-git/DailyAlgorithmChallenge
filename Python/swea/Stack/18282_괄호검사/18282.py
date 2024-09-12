import sys

sys.stdin = open('input.txt')


def checkcheck(check):
    stack = []
    # check의 char을 하나하나 비교해보기
    for char in check:
        # 만약 (가로가 나오면 stack에 쌓아주고
        if char == "(":
            stack.append('(')
        # ) 닫는 괄호가 나오면 stack에서 빼주고 count추가
        elif char == ')':
            if stack :
                if stack.pop() != '(':
                    return print(f'#{tc} -1')

            else:
                return print(f'#{tc} -1')
    if len(stack) != 0 :
        print(f'#{tc} -1')
    else: print(f'#{tc} 1')


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):


    # 스택을 짜주면됨.

    check = input().strip()
    checkcheck(check)

