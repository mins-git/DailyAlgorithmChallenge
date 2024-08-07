import sys

sys.stdin = open('input.txt')

def dfs(start) :  # 초기 시작하는값과 노드를 받아올것임.
    visited[start] = True
    result.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
    return result


T = 1

for tc in range(1, T+1):

    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    arr = list(map(int, input().split()))
    visited = [False] * (V+1) # 정점의 개수 만들어주기
    result = []
    for i in range(E):
        x, y = arr[i*2], arr[i*2+1]
        graph[x].append(y)
        graph[y].append(x)

    # print(graph)
    result = dfs(1)
    result = '-'.join(map(str, result))
    print(f'#{tc} {result}')

