import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start, V, graph): # start: 시작할점 V: 간선의 개수
    # 준비
    visited = [False] * (V+1) # visited 생성
    q = deque() # 큐생성
    q.append(start)# 시작점 인큐
    visited[start] = True   # 시작점 방문표시

    # 탐색
    while q: # 탐색할 정점이 남아있으면
        v = q.popleft()
        print(v, end=' ')# 디큐 첫번째꺼를 빼고 결과값에 저장하기
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


V, E = map(int, input().split())

node = list(map(int, input().split()))
adj_L = [[] for _ in range(V+1)] # 그래프를 그림

for i in range(E):
    v1, v2 = node[i*2], node[i*2+1]
    adj_L[v1].append(v2)
    adj_L[v2].append(v1)
print(f'#{1}', end = " ")
bfs(1, E, adj_L)

#1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7