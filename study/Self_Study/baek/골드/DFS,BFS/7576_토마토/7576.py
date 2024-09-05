import sys
sys.stdin = open('input.txt')
from collections import deque

# 상자의 가로, 세로
col, row = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(row)]

# 우 하 좌 상
dr = [0, 1, 0 , -1] # 행
dc = [1, 0, -1, 0] # 열

queue = deque() #deque([(3, 5)])

for i in range(row):
    for j in range(col):
        if box[i][j] == 1:
            queue.append((i, j))

# 아래 코드는 모든 익은 토마토를 추가하지 못했기 때문에 틀림.
# for i in range(row):
#     if 1 in box[i]:
#         queue.append((i, box[i].index(1)))

while queue:
    r, c = queue.popleft()
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < row and 0 <= nc < col and box[nr][nc] != -1 and box[nr][nc] == 0:
            box[nr][nc] = box[r][c] + 1
            queue.append((nr,nc))

max_days = 0
# 완전 탐색을 하면서
for r in range(row):
    for c in range(col):
        if box[r][c] == 0:
            print(-1)
            exit()
        max_days = max(max_days, box[r][c])

print(max_days -1)