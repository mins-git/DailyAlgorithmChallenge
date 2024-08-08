import sys
sys.stdin = open('input.txt')


# 결국 '.'만나면 연산 시작하는것임.
# 형식이 잘못되면 error
# '.'이 없을수도있고,
# 피연산자가 없는데 연산자가 남아잇음
# 피연산자가 있는데 연산자가 없음


def calcal(arr):
      # 후위 표기법
    for i in range(len(arr)):

            # 만약 피연산자면
            if arr[i] not in ['+', '-', '*', '/'] and arr[i] != '.':
                stack_num.append(int(arr[i]))  # ['10', '2', '3', '4']

            # 만약 연산자라면
            elif arr[i] in ['+', '-', '*', '/']:
                if len(stack_num) < 2: # 피연산자 2개보다 작으면
                    return 'error'

                a = stack_num.pop()  # 피연산자 제윌위 꺼내와서
                b = stack_num.pop()  # 피연산자 제일위 보다 한칸 아래 뽑기
                oper = arr[i]  # 연산자 뽑기

                if oper == '+':
                    stack_num.append(b + a)
                elif oper == '-':
                    stack_num.append(b - a)
                elif oper == '/':
                    stack_num.append(b // a)
                elif oper == '*':
                    stack_num.append(b * a)
            elif arr[i] == '.':
                if len(stack_num) >= 2:
                    return 'error'
                return stack_num[0]


T = int(input())
for tc in range(1, T+1):

    arr = list(map(str, input().strip().split())) #['10', '2', '+', '3', '4', '+', '*', '.']
    stack_num = []
    stack_oper = []
    if '.' not in arr: # .이 없는경우
        print(f'#{tc} error')
    print(f'#{tc} {calcal(arr)}')