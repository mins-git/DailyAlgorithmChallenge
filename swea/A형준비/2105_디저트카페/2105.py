import sys
sys.stdin = open('input.txt')

"""

- 원 안의 숫자는 해당 디저트 카페에서 팔고 있는 디저트의 종류 의미.
- 카페 투어 중 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안된다.
- 하나의 카페x
- 왔던길 되돌아가기 x 
- 디저트 최대한 많이 먹고싶음.
- 디저트 못먹으면 -1
"""

direction = [(1, -1), (-1, -1), (-1, 1), (1, 1)] # 시계방향 기준으로 12시 - 3시 / 3시 -6시 / 6시 - 9시 / 9시 - 12시


def dessert_ju_se_yo(i,j, visited):

    visited = [[False] * N for _ in range(N)]

    visited[i, j] = True

    # 방향 변경시 필요한 코드
    for k in range(4):

        nr = i + direction[k][0]
        nc = j + direction[k][1]
        arr = [cafe[i][j]]

        while 0 <= nr <= N and 0 <= nc < N: # 행렬안에 있고,
            if cafe[nr][nc] not in arr and # arr 배열에 없고,
    # if k + 1 >= 4:
    #     k = 0
    # else:
    #     k += 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    recent = []

    for i in range(N):
        for j in range(N):
            k = dessert_ju_se_yo(i, j)



