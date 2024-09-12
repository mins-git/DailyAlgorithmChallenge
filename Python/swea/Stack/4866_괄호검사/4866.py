import sys

sys.stdin = open('input.txt')

def checkcheck(str_in) :
    stack = []
    for char in str_in:
        if char == '(':
            stack.append(char)
        elif char == '{':
            stack.append(char)

        if char == ')':
            if stack:
                if stack.pop() != '(':
                    return print(f'#{tc} 0')
            else : return print(f'#{tc} 0')

        if char == '}':
            if stack:
                if stack.pop() != '{':
                    return print(f'#{tc} 0')
            else : return print(f'#{tc} 0')

    if len(stack) == 0 :
        return print(f'#{tc} 1')
    else: return print(f'#{tc} 0')



# Testcase 수

T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    str_input = input().strip()

    checkcheck(str_input)