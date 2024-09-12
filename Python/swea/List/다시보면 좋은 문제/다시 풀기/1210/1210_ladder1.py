import sys

sys.stdin = open('input.txt')



T = int(input())


for tc in range(1, T+1):

    ladder = [list(map(int, input().split())) for _ in range(100)] # 사다리 받기

    start = [99] #[99, 57]

    for i in range(100):
        if ladder[99][i] == 2:
            start.append(i) #[99, 57]

    recent_x = 99
    recent_y = start[1]

    dr = [0, 0, -1] # 오왼위
    dc = [1, -1, 0]


    # 값을 내것만 돌아야지. 문제점1. 100번만 반목하면 안됨. recentx가 0보다 클동안 계속가야지!
    while recent_x > 0 :
        for k in range(3): # 델타 진행
            nr = recent_x + dr[k] # 현재 위치에서 델타 체크해야지
            nc = recent_y + dc[k] # 현재 위치에서 델타 체크해야지
            if 0 <= nr < 100 and 0 <= nc < 100 and ladder[nr][nc] == 1:
                recent_x = nr  # 이동한 곳으로 값 저장
                recent_y = nc  # 이동한 곳으로 값 저장
                ladder[recent_x][recent_y] = 0  # 이동한곳 값 0으로 저장

    print(f'#{tc} {recent_y}')
