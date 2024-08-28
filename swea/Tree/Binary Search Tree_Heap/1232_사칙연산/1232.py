import sys
sys.stdin = open('input.txt')

"""
# 연결리스트 // 해당 부분 공부 필요
# 인접리스트
"""

# 중위탐색해보기 # “(9/(6-4))*3”
def inorder(node):
    global lst
    if node == 0:
        return
    inorder(int(left_node[node]))
    inorder(int(right_node[node]))
    lst.append(nodes[node])

# 테스트 케이스 수
T = 10

# 테이스 케이스 수 만큼 반복
for tc in range(1, T + 1):

    N = int(input()) # 5
    # 정점이 정수면 정점 번호와 양의 정수.
    # 정점이 연산자이면 정점 번호, 연산자, 해당점점의 왼쪽 정점번호 ,오른쪽 정점번호
    nodes = [0 for _ in range(N + 1)]
    left_node = [0 for _ in range(N + 1)] # [0] * (N+1)
    right_node = [0 for _ in range(N + 1)]

    # 트리모양 구축하기
    for i in range(N): # 정점의 개수만큼 반복할것임.
        random = input().split() #['5', '65']

        if random[1].isnumeric(): # 만약 random input값의 1번째가 숫자이면,
            nodes[i+1] = random[1]
        else:
            nodes[i+1] = random[1]
            left_node[i+1] = random[2]
            right_node[i+1] = random[3]

    lst = []
    inorder(1)
    stack = [int(lst[0])]

    for i in range(1, len(lst)):

        if lst[i] == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)

        elif lst[i] == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)

        elif lst[i] == '/':
            b = stack.pop()
            a = stack.pop()
            stack.append(a // b)

        elif lst[i] == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)

        else:
            stack.append(int(lst[i]))

    print(f'#{tc} {stack[0]}')

