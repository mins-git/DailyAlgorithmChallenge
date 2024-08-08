import sys

sys.stdin = open('input.txt')

def is_it_possible(arr):
    row, cols = len(arr), len(arr[0]) #지금 N * N 배열이기에 굳이 필요 없음.
    directions = [(0,1),(1,0),(0,-1),(-1,0)] # 시계방향 우 하 좌 상

    start, end = None, None
    for r in range(row):
        for c in range(cols):
            if arr[r][c] == 2:
                start = (r,c)
            elif arr[r][c] == 3:
                end = (r,c)

    stack = [start]
    visited = set([start])

    while stack:
        r, c = stack.pop() # 2가지 x,y를 뽑아서
        if(r,c) == end:
            return 1

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0 <= nc <cols and (nr, nc) not in visited and arr[nr][nc] != 1:
                stack.append((nr,nc))
                visited.add((nr,nc))
    return 0




T = int(input())

for tc in range(1, T+1):


    # N개의 미로
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start, end = None, None

    result = is_it_possible(arr)
    print(f'#{tc} {result}')
