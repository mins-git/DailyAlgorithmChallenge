import sys
import heapq
sys.stdin = open('input.txt')

"""
최적의 경로 이동시 최소한 연료 가능.

맨 왼족위에서 출발 > 가장 오른쪽 아래로 진행.

상하좌우 인접 지역으로만 이동 가능.
높이가 바뀌면 연료 추가로 +1

최소 연료 소비량 출력.
0,0  >N,N 으로 가야함.
작은 값으로만 이동하기.

r,c 좌표를 각각 노드로 확인하면서 이동하면 될듯? 비용도 체크해가면서.
비용은 area_height에 들어잇음.

"""
INF = int(1e9)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dijkstra(x,y):
    q = []
    distance[x][y] = 0
    heapq.heappush(q, (0, x, y))

    while q:
        cost, now_x, now_y = heapq.heappop(q)

        if cost > distance[now_x][now_y]:
            continue

        for k in range(4):
            nr = dr[k] + now_x
            nc = dc[k] + now_y
            if 0 <= nr < N and 0 <= nc < N:
                new_cost = cost + max(0, area_height[nr][nc] - area_height[now_x][now_y]) + 1

                if new_cost < distance[nr][nc]:
                    distance[nr][nc] = new_cost
                    heapq.heappush(q, (new_cost, nr, nc))

    return distance[-1][-1]

T = int(input())

for tc in range(1, T+1):


    N = int(input())
    area_height = [list(map(int, input().split()))for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]

    print(f'#{tc} {dijkstra(0,0)}')
