import sys

sys.stdin = open('input.txt')


# 계산식을 후위계산식으로 바꾸어 계산까지 완료하는 프로그램을 만드시오.

def change_huwiii(arr):
    result = '' #후위 계산식이 저장될것임.
    for i in range(len(arr)):
        if arr[i] == '+' :
            stack.append(arr[i]) # 연산자 스택에 추가해주기
        else : # 만약 피연산자이면
            result = result + arr[i]

    # 이러면 현재 stack에는 +가 순서대로 쌓이고, result에는 피연산자들이 들어가잇겟지?
    while len(stack) > 0 :
        result = result + stack.pop()

    return result


def calculate_huwiii(arr):
    for i in arr:           # arr 순회
        if i != '+':
            stack.append(int(i))  # temp에 피연산자만 넣어주기
        elif i == '+':  # 만약 연산자 발견시
            a = stack.pop()  # 1번째 pop한 요소
            b = stack.pop()  # 2번재 pop한 요소
            result = a + b # result에 a+b더한값 넣기.
            stack.append(a+b)  # 2번째요소가 먼저 들어간 피연산자이기에 2번재 + 1번재가됨.
    return result

T = 1
for tc in range(1, T+1):
    # 후위계산식으로 바꾸어 계산해서 정답출력.
    N = int(input())
    A = str(input()) #9+8+5+9+2+4+1+
    arr = []
    stack = []
    sum = 0
    # 각각의 요소 잘라줘서 리스트로 변환 필요
    for i in range(len(A)):
        arr.append(A[i]) #['9', '+', '8', '+', '5'

    # 후위계산식으로 바꾸기.
    hi_huwiii = change_huwiii(arr) # 985924183938786894117615876963131759284373473483266++++++++++++++++++++++++++
                                   # 후위계산 뱉는중

    # 새로운 arr 보내기
    new_arr = []
    # 각각의 요소 잘라줘서 hi_huwiii 리스트로 변
    for i in range(len(hi_huwiii)):
        new_arr.append(hi_huwiii[i])

    # 후위 표기법의 수식을 스택을 이용하여 다시 계산해보기
    # 현재 스택은 다시 비어있음
    print(f'#{tc} {calculate_huwiii(new_arr)}')
