import sys

sys.stdin = open('input.txt')


def postfix(munja):
    oper_stack = []
    output = []
    # tc만큼 순회
    for index in munja:

        # *가 곱하기는 바로뒤에 곱하기 두면되고,
        # +기도 숫자 바로뒤에 두면되지만, 그 사이 곱하기가 있따면 뛰어넘고 더하기두기

        # 변환해서 계산하기
        if index.isnumeric(): # 만약 인덱스가 숫자라면 append 하세요.
            output.append(index) # 피 연산자 넣기


        else:
            # 스택의 상단 연산자와 현재 연산자의 우선순위를 비교하여 처리
            while oper_stack and precedence[oper_stack[-1]] >= precedence[index]: # 연산자 스택의 제일 마지막것이 *라면?
                output.append(oper_stack.pop()) #
            oper_stack.append(index)

    # 중위 표기식의 모든 문자를 처리한 후, 스택에 남아 있는 모든 연산자를 출력 리스트에 추가
    while oper_stack:
        output.append(oper_stack.pop())

    return ''.join(output)




for tc in range(1, 11):
    # 테스트 케이스의 길이
    tc_len = int(input())
    munja = input()

    precedence = {'+': 1 , '*':2}
    for_calculate = postfix(munja)

    # 후위 계산식 계산하면됨. 이제
    calculate = [] # 출력할 변수
    oper_stack = []
    for i in for_calculate:
        if i.isnumeric(): #숫자면
            calculate.append(int(i)) # numstack에 추가하고

        else:
            if i == '*':
                num2 = calculate.pop()
                num1 = calculate.pop()
                calculate.append(num1 * num2) #계산한값 넣어주고

            elif i == '+':
                num2 = calculate.pop()
                num1 = calculate.pop()
                calculate.append(num1 + num2)  # 계산한값 넣어주고

    print(f'#{tc} {calculate[0]}')