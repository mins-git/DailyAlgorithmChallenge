import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
'''
6살 차윤이 왼 90도회전 오90도 회전 RC카 작년 생일 선물 받음

`최소 리모컨 조작 횟수임.`

n*n 크기 필드 정보 / 아빠 최대 벨 나무 수.
위를 바라보는 사앹로 rc 조작 시작

bfs를 이용하면서 
K를 1씩 빼면서 만약 K가 1이라면 더이상 이동 X 다른 경로 찾기.
'''

#  상(0) 우(1) 하(2) 좌(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    queue = deque()
    queue.append((my_position[0], my_position[1], 0, K, 0))

    visited.add((my_position[0], my_position[1], 0, K)) # 현재 노드 방문처리

    while queue:
        qx, qy, sdir, k, cnt = queue.popleft()

        if [qx, qy] == target_position:
            return cnt

        # 현재 바라보는 방햐으로의 이동
        nx, ny = qx + dx[sdir] , qy + dy[sdir]
        if 0 <= nx < N and 0 <= ny < N:
            if matrix[nx][ny] in ['G', 'Y'] and (nx, ny, sdir, k) not in visited:
                visited.add((nx, ny, sdir, k))
                queue.append((nx, ny, sdir, k, cnt+1))

            elif matrix[nx][ny] == 'T' and (nx, ny, sdir, k - 1) not in visited and k > 0:
                visited.add((nx, ny, sdir, k - 1))
                queue.append((nx, ny, sdir, k - 1, cnt + 1))

        ndir_left = (sdir -1) % 4
        if (qx, qy, ndir_left, k) not in visited:
            visited.add((qx, qy, ndir_left, k))
            queue.append((qx, qy, ndir_left, k, cnt +1))

        ndir_right = (sdir + 1) % 4
        if (qx, qy, ndir_right, k) not in visited:
            queue.append((qx, qy, ndir_right, k, cnt + 1))
    return -1



T = int(input())

for tc in range(1, T+1):
    N, K  = map(int,input().split())

    matrix = [list(input()) for _ in range(N)]
    visited = set()


    for x in range(N):
        for y in range(N):
            if matrix[x][y] == 'X':
                my_position = [x,y]
            elif matrix[x][y] == 'Y':
                target_position = [x,y]

    result = bfs()

    print(f'#{tc} {result}')