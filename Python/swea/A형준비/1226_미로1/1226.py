import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


'''
흰 바탕은 길 노란 바탕은 벽
좌상단 0,0 기준으로 가로 x 세로 y
1,1 에서 시작. // 1은 벽 0은길 //2는 출발점 // 3은 도착점

도착 가능시 1 못하면 0
'''

T = 10

direction = [(0,1), (1,0), (0,-1), (-1,0)]

def bfs(start_x, start_y, end_x, end_y):



    queue = deque([(start_x, start_y)])
    visited = [[False] * 16 for _ in range(16)]
    visited[start_x][start_y] = True # 시작지점 True 초기화

    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            return True

        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]

            if 0 <= nx < 16 and 0<= ny < 16 and not visited[nx][ny] and matrix[nx][ny] != 1:
                visited[nx][ny] = True
                queue.append((nx,ny))

    return False


for tc in range(1, T+1):
    # 무조건 1,1 시작
    # 델타 탐색으로 갈 수 있으면 이동하면됨 막힌길이면 돌아오면됨.
    # DFS > 깊이우선탐색
    # BFS > 도달
    a = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(16)]
    end_x, end_y = -1, -1 # 초기화 13 13


    for i in range(16):
        if 3 in matrix[i]:
            end_x = i
            end_y = matrix[i].index(3)
            break


    if bfs(1, 1, end_x,end_y):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
