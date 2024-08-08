# 코드

- 문제 풀이 포인트 🤞
    1. pop전에 피연산자가 2개보다 작으면 오류가 날 것 포인트!
    2. ‘.’이 없어도 오류가 발생해야됨.
    3. ‘.’을 만났는데, stack에 자료가 2개이상 남아있으면 error 출력!
- 앗 나의 실수 😢
    1. 자꾸 오류가 떠서 확인해보니 나누기할때 / 로 출력하면 float이 나온다! float이 아닌 int를 뽑기위해서는 //로 지정해야됨. (*문제에서 나머지가 없다라고 명시함)
    

```python
#1.

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

```