import sys
sys.stdin = open('input.txt')
from collections import deque
"""
 n x n 미로가 있음.
 1은 이동가능 0은 이동불가.
 조건
 - (1,1) 출발. n,m으로 이동할때 지나야하는 최소 칸수? 시작위치 도착위치도 포함!
 
"""

row , col = map(int, input().split())
maze = [list(input().strip()) for _ in range(row)]

# print(maze)

dr = [0 , 1, 0, -1]
dc = [1, 0, -1, 0]

queue = deque()

queue.append((0, 0))

while queue:
    r, c = queue.popleft()

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr <= row-1 and 0 <= nc <= col-1 and maze[nr][nc] != 0 and maze[nr][nc] == '1':
            maze[nr][nc] = int(maze[r][c]) + 1
            queue.append((nr, nc))

print(maze[row-1][col-1])