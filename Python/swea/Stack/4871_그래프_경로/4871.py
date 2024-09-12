import sys

sys.stdin = open('input.txt')



T = int(input())

for tc in range(1, T+1):

    # V개의 노드 / E개의 줄
    V, E = map(int, input().split())

    # E개의 줄에 걸쳐 출발 도착 노드로 간선 정보 주어짐.
    arr = [list(map(int,input().split())) for _ in range(E)]
    graph = [[] for _ in range(V+1)]
    print(arr)
    print(graph)
    for i in range(E):
        x, y = arr[i*2], arr[i*2+1]
        graph[x].append(y)
        graph[y].append(x)
    # print(graph)
    # 출발노드 s와 도착노드 g가주어짐.
    S, G = map(int,input().split())

    # 두개의 노드에 경로가 존재하니? 하면1 아니면 0

    # dfs 를 통해서 깊이를 탐색하는데,
    # 인접리스트에 겹치는게 있을까?를 찾으면 됨.
