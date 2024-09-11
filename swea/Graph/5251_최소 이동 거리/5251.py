import sys
import heapq
sys.stdin = open('input.txt')


"""
n은 노드의 수  (01,2)
e는 간선의 수 
0번부터 N번까지의 번호가 붙음.
0 > n까지 이동하는 최소거리 얼마? 
"""

INF = int(1e9)

T = int(input())

for tc in range(1, T+1):
    # N: 노드수 / E: 간선수 # 노드는 0부터 시작함. 0-based
    N, E = map(int, input().split())
    distance_list = [list(map(int, input().split())) for _ in range(E)]

    distance = [INF] * (N+1)
    graph = [[] for _ in range(N+1)]

    for a, b, c in distance_list:
        graph[a].append([b, c])

    def dijkstra(start):

        q = []
        distance[start] = 0
        heapq.heappush(q, (0, start))

        while q:

            dist, now = heapq.heappop(q)

            if dist > distance[now]:
                continue

            for i in graph[now]:
                next_node = i[0]
                cost = i[1]

                new_cost = dist + cost

                if new_cost < distance[next_node]:
                    distance[next_node] = new_cost
                    heapq.heappush(q, (new_cost, next_node))

    dijkstra(0)

    print(f'#{tc} {distance[N]}')