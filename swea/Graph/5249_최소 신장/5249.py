import sys
import heapq
sys.stdin = open('input.txt')


#  사이클 제거 > 모든 노드 포함하는 트리 구성> 가중치의 합이 최소

INF = int(1e9)

def prim(start):
    q = []
    visited = [False] * (V+1)
    total_cost = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if visited[now]:
            continue
        visited[now] = True
        total_cost += dist
        for next in range(V+1):
            if graph[now][next] == 0:
                continue
            if visited[next]:
                continue
            heapq.heappush(q, (graph[now][next], next))
    return total_cost

T = int(input())

for tc in range(1, T+1):
    # 노드번호 0 ~  V / 간선의 개수 E
    V, E = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(E)]
    graph = [[0] * (V+1) for _ in range(V+1)]
    for i in matrix:
        u, v, w = i
        graph[u][v] = w
        graph[v][u] = w

    result = prim(0)

    print(f"#{tc} {result}")