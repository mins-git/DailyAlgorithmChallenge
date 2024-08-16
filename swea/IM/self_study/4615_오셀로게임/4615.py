import sys

sys.stdin = open('input.txt')

"""
board = 4*4 6*6 8^8 사용함.


WB
BW 와 같이 배열 놓고 시작.
가로, 세로, 대각선 파악 필요함.
COL, ROW 식으로 INPUT 되고있음. (2,3)

1. 놓아지는 좌표에서 델타를 활용해서, 위로 8방향으로 겹치는곳 있나 체크해야됨.
2. 바로 오른쪽에 다른 색상이면 진행가능. 아니면 break
3. 오른쪽에 같은색상이 있을때까지. 만약 벽까지 이동하는데 같은색상이 없거나 빈공간이면 break
4. 같은색상이 있으면 해당 위치 적혀져있는 [2]번째 인덱스로 해당줄 전부 변경하기.
"""

B = 1 # 흑돌
W = 2 # 백돌

dr = [0,1,1,1,0,-1,-1,-1] # 오른쪽부터 한바퀴 회전
dc = [1,1,0,-1,-1,-1,0,1]


def othello(r, c, color):
    board[r][c] = color # 현재 들어온 값 위치에 색 넣어주기

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]  # 다음 칸 색상 체크해보기

        while 0 <=  nr < N and 0 <= nc < N and board[nr][nc] != color and board[nr][nc] != 0 : # 배열을 벗어나지 않고, 색상이 다르다면
                nr += dr[i]  # 해당 방향으로 계속 진행
                nc += dc[i]


                # 방향에 끝에 도달햇을때, 마지막 색상이 같은 색상이면
                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == color:
                    nr -= dr[i]
                    nc -= dc[i]
                    while (nr,nc) != (r,c):
                        board[nr][nc] = color # 색상 해당 돌로 바꿔주기
                        nr -= dr[i]
                        nc -= dc[i]
                    break



# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 보드의 한변의 길이 N, 플레이어 돌을 놓는 횟수 M이 주어짐.
    board = [[0]* N for _ in range(N)] # 보드 생성
    dol = [list(map(int,input().split())) for _ in range(M)]
    # 1, 2, 1 이면,
    # 2가 col 1이 row 흑돌임.

    # n이 4이거나, ndl 6이거나 8이거나 존재

    #처음 돌위치 중간에 설정하기,
    board[N//2 -1][N//2 -1] = W
    board[N//2-1][N//2] = B
    board[N//2][N//2-1] = B
    board[N//2][N//2] = W


    for x, y, c in dol:
        othello(y-1, x-1, c)

    black = 0
    white = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                black += 1
            elif board[i][j] == W:
                white += 1

    print(f'#{tc} {black} {white}')
