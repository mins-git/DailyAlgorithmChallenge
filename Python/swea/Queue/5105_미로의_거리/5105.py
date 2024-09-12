import sys
sys.stdin =  open('input.txt')


"""
N*N 크기의 미로에서 출발지 목적지가 주어짐.
최소 몇개의 칸을 지나야 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램.
1은 벽 0은 통로 미로밖 벗어나지마

"""

from collections import deque

def bfs(start):
    q = deque() # 덱 만들어주기
    q.append(start) # start 추가해주기
    visited = [[0] * N for _ in range(N)] # 똑같은 위치에 넣어줘도 괜찮아. 그래프 아니잖아.
    visited[start[0]][start[1]] = 1 # start는 현재x,y두개가 들어오고 있음

    while q: # q 가 비지 않은 선에서 진행해보기
        x, y = q.popleft() # 디큐를 진행하여 v에 값 담아주기. # 초기값은 r_x, r_y 숫자 2가있는게 들어와있을거야.

        if matrix[x][y] == 3:
            return visited[x][y] -1 -1
        for dr, dc in [[-1,0], [1,0], [0,-1], [0,1]]: # 상하좌우 위치 전환하면서
        # for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:  # 오아왼위 위치 전환하면서
            nr = x + dr
            nc = y + dc

            if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] != 1 and visited[nr][nc] == 0:

                q.append([nr,nc]) # 해당 값을 덱에 추가해주고, 인큐하는데 터질수가있나
                visited[nr][nc] = visited[x][y] + 1
    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,''.join(input().split()))) for _ in range(N)]
    r_x = 0
    r_y = 0

    for x in range(N): # x, y 값 찾아주기
        for y in range(N):
            if matrix[x][y] == 2:
                r_x = x
                r_y = y

    start = [r_x, r_y] # 현재값 담아주기.

    print(f'#{tc} {bfs(start)}')
