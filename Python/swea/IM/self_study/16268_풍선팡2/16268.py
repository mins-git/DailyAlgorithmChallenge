import sys
sys.stdin = open('input.txt')




T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    flower_max_count = 0

    for r in range(N):
        for c in range(M):
            flower_count = arr[r][c]
            for dr, dc in [[0,1], [1,0], [0,-1], [-1,0]]:
                nr, nc = r+dr , c+dc
                if 0<=nr<N and 0<=nc<M:
                    flower_count += arr[nr][nc]

            if flower_count > flower_max_count:
                flower_max_count = flower_count

    print(f'#{tc} {flower_max_count}')