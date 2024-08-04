import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T + 1):

    # 출발점의 x좌표 출력하는 문제!

    # 아래 코드 알고리즘:

    # 1. 마지막행의 열중 2를 찾기!
    # 2. 델타 사용해서 오른쪽 왼쪽 위 순서로 이동.
    # 3. 이동시에 조건문 생성
    # 3.1 조건문1. 만약 빈배열 확인시 간적 없어야 이동해!
    # 3.2 조건문2. 오른쪽 왼쪽 위 순서로 찾은 값이 1이라면 해당 값으로; 이동할거야!
    # 4. 해당 값에 현재 위치 재설정!

    test_cast = int(input())

    # 사다리 입력 받기!
    ladder = [list(map(int, input().split())) for _ in range(100)]  # 2차원 배열 생성
    already_go = [[0] * 100 for _ in range(100)]  # 빈 100배열 체크
    X = 0  # x의 열 인덱스
    # 마지막줄 열중 2를 찾을거야!
    for c in range(100):
        if 2 == ladder[99][c]:
            X = c  # 57번째가 2임.

    delta_x = 99
    delta_y = X

    # 행을 -1해가면서 요소 좌우측에 1이있으면 해당 방향으로 이동 없으면 위쪽 1로 이동!
    # 조건은, 0의값과 100의 값을 넘으면 안돼! + 좌우측 0이 있으면 이동하지 않아!

    dr = [0, 0, -1]  # 오른쪽 왼쪽 위 탐색
    dc = [1, -1, 0]  # 오른쪽 왼쪽 위 탐색

    # x가 0에 도달하지 않을때까지 이동하기.
    while delta_x > 0:
        already_go[delta_x][delta_y] = 1  # 빈 배열에 x,y를 체크해 준 후 이미 간곳은 빈 배열에 저장하기!

        # 현재 위치에서 delta검색을 하면 되잖아?
        for k in range(3):  # 오른쪽 왼 쪽 위 델타 체크
            nr = delta_x + dr[k]
            nc = delta_y + dc[k]
            if 0 <= nr < 100 and 0 <= nc < 100:  # 벽 양측, 위 부딪히지 않은 상태로 델타진행!

                if already_go[nr][nc] != 1:  # 만약 간적이 없는곳이라면 # 이미간곳 안 가기
                    if ladder[nr][nc] == 1:  # 만약 델타로 찾은 값이 1이라면 해당 if문진행!

                        delta_x = nr  # x에 nr인덱스 넣기
                        delta_y = nc  # y에 nc인덱스 넣기

    print(f'#{test_cast} {delta_y}')








    # 연습하던 코드 아래


    # for r in range(100, 0, -1): # 100부터 시작해서 0까지 -1 행을 -1하면서 올라갈것임.
    #     for c in range(100): # 열도 체크해야지 옆의 값이 0인지 봐야지!
    #         for k in range(4): # 오른쪽 아래 왼쪽 위 탐색함!
    #             nr = r + dr[k]
    #             nc = c + dc[k]
    #             if 0 <= nr < 100 and 0 <= nc < 100 : # 벽 양측, 위 아래 부딪히지 않은 상태로 델타진행!
    #                 if (ladder[r-1][c] == 1 and ladder[r][c-1] == 1) or (ladder[r-1][c] == 1 and ladder[r][c+1] == 1):# 만약 위도 1이고, 좌,우측도 1이라면 위는 가지마!
    #                     ladder[r-1][c] = 0 # 위를 0으로 바꿔주기
    #
    #                 if already_go[nr][nc] != 1: # 만약 간적이 없는곳이라면
    #                     if ladder[nr][nc] == 1: # 만약 델타로 찾은 값이 1이라면 해당 if문진행!
    #                         already_go[nr][nc] = 1 # 이미 온곳에 1체크하기! (# 빈 배열에 해당 좌표값에 1을 저장해!(좌우측에 1이 있으면! 해당 인덱스로 이동해!))
    #                         ladder[r][c] == 0
    #                         delta_x = nr
    #                         delta_y = nc
    #                         # #좌우측에 1이 있으면 해당 인덱스로 이동. 단, 이미 지나왔던곳이라면 가면 안됨! (뒤로가겠지?)

    # if (ladder[delta_x][delta_y-1] == 1 and ladder[delta_x - 1][delta_y] == 1) or (ladder[delta_x][delta_y+1] == 1 and ladder[delta_x-1][delta_y] == 1):  # 만약 위도 1이고, 좌,우측도 1이라면 위는 가지마!
    #     ladder[delta_x-1][delta_y] = 0  # 위를 0으로 바꿔주기
    # if ladder[nr][nc] == 1
