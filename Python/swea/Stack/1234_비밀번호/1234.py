import sys

sys.stdin = open('input.txt')


# Testcase 수
T = 1
# Testcase 만큼 반복
for tc in range(1, T+1):


    N, M = map(str, input().split())
    M_list = list(M)

    # 스택을 활용해서 중간에 같은 문자 제거해버리기.
    stack = []

    # N 글자 순회
    for i in range(int(N)):
        # 만약 스택안에 아무것도 없으면 추가해줘.
        if len(stack) == 0:
            stack.append(M_list[i])
        # 만약 스택의 마지막요소와 m의 현재 요소가 같으면
        elif stack[-1] == M_list[i]:
            stack.pop()
        #만약 스택의 마지막 요소와 m의 현재 요소가 같지 않으면,
        else: stack.append(M_list[i])




    result = ''.join(stack)
    print(f'#{tc} {result}')


    # print(stack) #['1', '2', '3', '4']
    # result = ''
    # for char in stack:
    #     result = result + char
    # print(f'#{tc} {result}')