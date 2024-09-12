import sys
sys.stdin = open('input.txt')

"""
시계방향으로 돌아가면서 순서대로 배정
1열 다 채우고 2열채우는식으로 갈것임.

달팽이네?
대기순서 K인사람의 좌석번호는?
"""


x, y = map(int, input().split())
K = int(input())

if K == 1:
    print(1, 1)
elif K > x * y:
    print(0)

else:
    # 인덱스로 계산하니 출력값은 x,y에 +1씩 해야됨.
    stadium = [[0] * x for _ in range(y)]

    dr = [-1, 0, 1, 0 ] # 위오아왼
    dc = [0, 1, 0, -1]
    direction = 0
    r = y-1 # 왼쪽 아래에서 시작해야지 1뺀거는 인덱스차이때문에
    c = 0
    stadium[r][c] = 1
    seat_num = 2  # 좌석번호

    while seat_num <= x*y:
        nr, nc = r + dr[direction], c + dc[direction]

        if 0 <= nr < y and 0<= nc < x and stadium[nr][nc] == 0: # 배열을 벗어나지 않는 동안 진행 한방으로 진행 필요
            stadium[nr][nc] = seat_num
            r, c = nr, nc # 현재위치 꼭 업데잍트 해주기

            if seat_num == K:
                print(c+1, y-r)
                break
            seat_num += 1
        else:
            direction += 1

            if direction == 4:
                direction = 0

    if seat_num > x*y:
        print(0)