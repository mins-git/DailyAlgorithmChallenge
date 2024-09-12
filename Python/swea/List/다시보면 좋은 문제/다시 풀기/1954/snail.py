import sys

sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):

    # 오른쪽으로 쭉가고
    # 아래로 쭉가고
    # 왼쪽 쭉가고
    # 위로 가면돼!
    # 단 위 4방향을 틀때에, 0이아니면 가지마 그때까지 반복!



    N = int(input()) # N*N 배열이 사용될것임.

    arr = [[0 * N for _ in range(N)]for _ in range(N)] # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # arr2 = [[0] * N for _ in range(N)]
    # # print(arr)
    # print(arr2)

    dr = [0, 1, 0, -1] # 오른쪽 아래 왼쪽 위
    dc = [1, 0 ,-1, 0]

    recent_x = 0
    recent_y = 0
    direction = 0 # 방향 인덱스 필수!
    num = 1

    for _ in range(N*N): # 전체 배열을 탐색할거야.
        arr[recent_x][recent_y] = num # arr의 현재 값에 1을 적어줄거고.
        num += 1 # num값도 1 추가해줄래.

        nx, ny = recent_x + dr[direction], recent_y + dc[direction] # nx, ny에 방향을 제시해주면돼! 현재 오른쪽으로 설정됐어. direction이 1이잖아.

        if not(0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0): # 만약 (다음값이 0이거나, 범위이내가) 아니라면
            direction = (direction +1) % 4 # 방향을 전환할거야.
            nx, ny = recent_x + dr[direction], recent_y + dc[direction] # 각 값에 새로운 nextx와 y를 넣어주고

        recent_x,recent_y = nx, ny # 이동시켜

    for row in arr:
        print(row)



