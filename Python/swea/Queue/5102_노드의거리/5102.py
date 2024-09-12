

"""
정점(노드)의 개수 = V
간선 E
몇개의 간선 이후에 도착 노드에 갈 수 있니?
"""

import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(S, G, V):
    q = deque() # 덱 생성하고
    q.append(S) # start값 넣어주기
    visited = [0] * (V+1) # visited를 노드의 1개만큼 더 생성해줘서 인덱스 기준으로 노드 숫자와 맞춰주기
    visited[S] += 1 # visited르 1로 설정해주기


    while q:
        current = q.popleft() # 디큐한 이후에
        if current == G: # 만약 현재자리랑 g가 같다면,
            return visited[G]-visited[S]
        for i in adj_L[current]:
            if not visited[i]: # 만약 방문한적이 없으면
                visited[i] = visited[current] + 1 # visitied +1하면됨.
                q.append(i)
    return 0


T = int(input())

for tc in range(1, T+1):

    V, E = map(int, input().split())# V는 노드의 개수 (정점의 개수) # E 줄에 걸쳐 간선의 양쪽 노드 번호가 주어짐
    node = [int(x) for _ in range(E) for x in input().split()]
    S, G = map(int, input().split()) #S는 출발노드, E는 도착 노드
    adj_L = [[] for _ in range(V+1)] # 노드의 개수 +1개로 만들기.
    for i in range(E) :
        x, y = node[i*2], node[i * 2 + 1] # [[1,4] . [2,3]] 이런식으로 있는게,
        adj_L[x].append(y)
        adj_L[y].append(x)

    result = bfs(S,G,V)
    print(f'#{tc} {result}')

