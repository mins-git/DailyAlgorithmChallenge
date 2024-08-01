import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 위의 리스트 컴프리헨션으로 사용.
    # arr = []
    # for i in range(N):
    #     arr.append(list(map(int, input().split())))

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    sum_arr = []
    result_sum =0

    # 배열 전체 탐색하기.
    for r in range(N):
        for c in range(N):
            for k in range(4):
               x = r + dr[k] # 오 아 왼 위
               y = c + dc[k] # 오 아 왼 위
               if 0 <= x < N and 0 <= y < N :
                   sum_arr.append(abs(arr[r][c] - arr[x][y]))


    for sum_num in sum_arr:
        result_sum += sum_num

    print(f'#{tc} {result_sum}')