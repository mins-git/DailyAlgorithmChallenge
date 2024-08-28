import sys
sys.stdin = open('input.txt')


"""
in-order 형식 순회 (중위순회 하라는것)
"""
def add_edge(adj_list, u, v):
    if u not in adj_list:
        adj_list[u] = []

    adj_list[u].append(v) # 방향 그래프로 u에서 v로 간선추가


def dfs(graph, node, visited = None):
    if visited is None:
        visited = []
    if node in graph: # 값이 있으면 시작
        child = graph[node]
        if len(child) > 0:
            dfs(graph, child[0], visited)
        visited.append(node)
        if len(child) > 1:
            dfs(graph, child[1], visited)
    else:
        visited.append(node)
    return visited



T = 10

for tc in range(1, T+1):

    N = int(input()) # 정점의 총 수
    arr = [list(map(str, input().split())) for _ in range(N)] # [['1', 'W', '2', '3'], ['2', 'F', '4', '5'], ['3', 'R', '6', '7'],
    alpha = [[0] for _ in range(N+1)] # 문자 저장할 변수 #[[0], [0], [0], [0], [0], [0], [0], [0], [0]]

    # ['2', 'F', '4', '5'] 2는 4 > 5 랑 이어졌다는것!

    # 그래프로 표현 필요함.
    #인접 리스트 담을 변수
    adj_list = {} # {'1': ['2', '3'], '2': ['4', '5'], '3': ['6', '7'], '4': ['8']}

    # 이진 트리여서 가능한 for문임
    for i in range(N):
        if len(arr[i]) == 2:
            alpha[i+1] =  arr[i][1] # [[0], [0], [0], [0], [0], 'T', 'A', 'E', 'S']

        elif len(arr[i]) == 3:
            alpha[i + 1] = arr[i][1]
            add_edge(adj_list, arr[i][0], arr[i][2])


        elif len(arr[i])== 4:
            alpha[i + 1] = arr[i][1]
            add_edge(adj_list, arr[i][0], arr[i][2])
            add_edge(adj_list, arr[i][0], arr[i][3])


    # 중위순회면 > 8 4 2 5 1 6 3 7
    result_arr = dfs(adj_list, '1') #['8', '4', '2', '5', '1', '6', '3', '7']
    result = ''
    for i in range(len(result_arr)):
        result += alpha[int(result_arr[i])]
    print(f'#{tc} {result}')




# -------------------------------------------------------
# 참고하면 좋은 코드

# # 중위 순회 => 왼쪽 -> 자신 -> 오른쪽
# def inorder(node):
#     # 자식이 없는 경우
#     if not graph[node]:
#         return
#     # 왼쪽에 자식이 있는지 확인
#     inorder(int(graph[node][1]))
#     # 문자 출력
#     print(graph[node][0], end="")
#     # 오른쪽에 자식이 있는지 확인
#     inorder(int(graph[node][2]))
