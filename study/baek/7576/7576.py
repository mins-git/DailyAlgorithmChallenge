import sys

sys.stdin = open('input.txt')


# 익은토마토 4방향의 익지않은 토마토가 있으면 다 익음.

# 1 = 익은 토마토
# 0 = 익지 않은 토마토
# -1 = 토마토가 들어있지 않음.




M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


for r in range(M):
    for c in range(N):
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if nr
