


"""

16 16 행렬로 만들어진 미로에서 0은길 1은벽

시작 1,1 에서 2에서시작함.
도착 13,13에 도착함.

갈 수 있는 길인지 판단하는 프로그램 작성

1.

"""

import sys

sys.stdin = open('input.txt')
from collections import deque


# 라이브 강사님 bfs
# start = 시작지점 인덱스 배열, end: 도착지점 인덱스 배열
# matrix = 2차원 배열 N = 배열 한변의 크기

def bfs(start, end, matrix, N):
    visited = [[False]*N for _ in range(N)]
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        now = q.popleft() # 현재 왼쪽에 있는것 디큐
        if now == end:
            return 1
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx = now[0] + dx # now는 현재 x y로 표현됨
            ny = now[1] + dy #
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != 1 and not visited[nx][ny]:
                q.append([nx,ny])
                visited[nx][ny] = True
    return 0




T = 10

for tc in range(1, T+1):
    TC = int(input())
    N = 16
    matrix = [list(map(int, input())) for _ in range(N)]
    start = [1,1]
    end = [13,13]
    print(f'#{TC} {bfs(start, end, matrix, N)}')