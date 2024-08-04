import sys

sys.stdin = open('input.txt')


T = 10

for tc in range(1, T+1):

    # N = 100 * 100
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range (100)]

    # 출력할 최대 값
    max_num = 0


    # 우측으로 쭉 더하기
    recent_x = 0
    recent_y = 0
    direction = 0

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1 ,0]

    # 가로더하기 #1704
    for r in range(100):
        #sum 초기화
        sum = 0
        for c in range(100):
            # 가로만 더하는 방법이 필요해.
            sum += arr[r][c]
        if sum > max_num:
            max_num = sum

    # 세로 더하기
    for c in range(100):
        sum = 0
        for r in range(100):
           sum += arr[r][c]

        if sum > max_num:
            max_num = sum


    # 대각선 더하기
    sum = 0
    for r in range(100):

        for c in range(100):
            if r == c :
                sum += arr[r][c]
    if sum > max_num:
        max_num = sum


    # 반대졲 대각선 더하기
    sum = 0
    for r in range(100):
        for c in range(100):
            if r == c :
                sum += arr[r][100- 1- r]

    if sum > max_num:
        max_num = sum


    print(f'#{test_case} {max_num}')