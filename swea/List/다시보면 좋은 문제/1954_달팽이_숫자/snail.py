import sys

sys.stdin = open('input.txt')




# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):


    # 문제 처리:
    # 달팽이는 밖에서부터 안으로 돎
    # 1 <= N <= 10
    # 문제 풀이 과정.
    # 1. 배열 밖을 벗어나면 방향전환
    # 2. 이전에 왔던곳이면 방향전환 (다음값이 0 인지로 체크해줌.)

    # N input값 설정
    N = int(input())
    # 빈배열로 0 꽉 채워주기
    snail_arr = [[0] * N  for _ in range(N)]
    snail_x = 0
    snail_y = 0

    dr = [0, 1 , 0, -1] #오 아 왼 위
    dc = [1, 0, -1, 0] # 오 아 왼 위
    direction = 0 # 초기 방향은 오른쪽.

    num = 1
    count = N * N

    # num는 현재 배열보다 작아야함.
    while num <= count:

        snail_arr[snail_x][snail_y] = num

        next_x = snail_x + dr[direction]
        next_y = snail_y + dc[direction]

            # 0 <= next_x < N and 0 <= next_y < N and snail_arr[next_x][next_y] == 0)

        if not(0<= next_x < N and 0 <= next_y < N and snail_arr[next_x][next_y] == 0): #범위밖 or 이미 방문한 경우
            direction = (direction + 1) % 4  # 방향 전환
            next_x = snail_x + dr[direction]
            next_y = snail_y + dc[direction]

        snail_x = next_x
        snail_y = next_y

        num += 1

    print(f'#{tc}')
    for row in snail_arr:
        print(' '.join(map(str, row)))