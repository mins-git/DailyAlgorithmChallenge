import sys
sys.stdin = open('input.txt')

"""
트리의 일부를 서브 트리라고 한다.
N을 루트로하는 서브 트리에 속한 노드의 개수?
"""

def check_node(graph, N): # {2: [1, 5], 1: [6], 5: [3], 6: [4], 3: [], 4: []}

    # 리스트에 자식 노드가 있는지 확인
    children = graph.get(N, []) # default를 []지정.

    if not children:
        return 1 # 특정 노드가 자식 노드가 없으면 자신의 개수인 1을 반환해줌.

    # 자식 노드 수 세기
    count = 1
    for child in children:
        count += check_node(graph, child)

    return count
# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 간선의 개수 E, N
    E, N  = map(int, input().split())
    # 간선의 개수 E, N
    arr = list(map(int, input().split()))

    adj_list = {}

    for i in range(0, E*2 -1, 2):
        u = arr[i]
        v = arr[i+1]

        if u not in adj_list:
            adj_list[u] = []
        if v not in adj_list:
            adj_list[v] = []

        adj_list[u].append(v)
        # adj_list[v].append(u)

    count = 0

    print(f'#{tc} {check_node(adj_list, N)}')