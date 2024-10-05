import sys
sys.stdin = open('input.txt')


'''
또 나온 차윤이

A : 앞으로 이동
L : 현재 바라보는 방향에서 왼쪽으로 90도 회전
R : 현재 바라보는 방향에서 오른쪽 90도 회전

항상 위를 바라보는 방향으로 부터 조종 시작
목적지 도달 가능여부 구하기 
'''

# 오 0 아 1 왼 2 위 3

dx = [0, 1, 0 , -1]
dy = [1, 0 , -1, 0]
T = int(input()) ## 테스트 케이스


for tc in range(1, T+1):
    N = int(input())  # 필드크기
    matrix = [list(input()) for _ in range(N)] # 필드 정보
    Q = int(input()) # 조종을 한 횟수
    command = [list(map(str, input().strip().split())) for _ in range(Q)] #[['7', 'RRAALAA'], ['8', 'RRAALAAA'], ['12', 'RAARRALAALAA']]
    result = []
    for x in range(N):
        for y in range(N):
            if matrix[x][y] == 'X':
                start_position = [x,y]
            elif matrix[x][y] == 'Y':
                end_position = [x,y]


    for move in range(Q):
        new_xy = start_position[:]
        direction = 3
        for command_cnt in command[move][1]:
            if command_cnt == 'R':
                direction += 1
                if direction == 4:
                    direction = 0
            elif command_cnt == 'L':
                direction -= 1
                if direction == -1:
                    direction = 3
            elif command_cnt == 'A':
                nx = new_xy[0] + dx[direction]
                ny = new_xy[1] + dy[direction]
                if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != 'T':
                    new_xy[0] = nx
                    new_xy[1] = ny
            else:
                continue


        if new_xy == end_position:
            result.append(1)
        else:
            result.append(0)

    print(f'#{tc} '+ ' '.join(map(str, result)))





