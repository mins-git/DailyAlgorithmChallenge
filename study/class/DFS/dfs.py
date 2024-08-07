'''
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def DFS(v):          # v: 방문 정점
    # 방문처리
    visited[v] = True
    result.append(v) #방문 정점 저장
    #다음 갈 곳을 확인
    for next in adjL[v]:
        #다음 갈곳이 방문하지 않았다면
        if visited[next] ==False:
                DFS(next)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]
    arr = list(map(int, input().split()))
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)

    visited = [False] * (V+1)
    result = [] #방문순서를 기록하기 위한 result
    DFS(1)

    print(*result)