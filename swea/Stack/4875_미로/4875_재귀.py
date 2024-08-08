import sys

sys.stdin = open('input.txt')

def dfs(r, c, visited):

    if (r, c) == end:
        return True
    visited.add((r, c))  # 현재위치 방문했다로 말해주고

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited and arr[nr][nc] != 1:
            if dfs(nr, nc, visited):
                return True

    return False


T = int(input())

for tc in range(1, T+1):


    # N개의 미로
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start, end = None, None

    # 방향지정
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1 ,0]

    # 숫자 2 찾아주기
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2 :
                start = (r, c)
            elif arr[r][c] == 3:
                end = (r, c)

    # dfs : 탈출할 수 있는 방법의 수 체크
    # bfs : 빠르게 가는법을 찾기

    # 인덱스 값이 3인곳에 갈 수 있니? 방법의 수 체크?
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1 ,0]

    visited = set()
    stack = []

    T_F = dfs(start[0], start[1], visited)
    if T_F is True:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
