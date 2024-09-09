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
#
# direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # 시계방향 기준으로 12시 - 3시 / 3시 -6시 / 6시 - 9시 / 9시 - 12시
#
#
# def dessert_ju_se_yo(i,j, start_i, start_j, visited,N, cafe):
#
#     if i == start_i and j == start_j and len(visited) > 0:
#         return len(visited)
#
#     max_length = 0
#
#     # 방향 변경시 필요한 코드
#     for k in range(4):
#
#         nr = i + direction[k][0]
#         nc = j + direction[k][1]
#         if 0 <= nr < N and 0 <= nc < N and (nr,nc) not in visited:
#             if cafe[nr][nc] not in visited:
#                 visited.add(cafe[nr][nc])
#                 max_length = max(max_length, dessert_ju_se_yo(nr,nc, start_i,start_j,visited,N,cafe))
#                 visited.remove(cafe[nr][nc])
#     return max_length
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     cafe = [list(map(int, input().split())) for _ in range(N)]
#     max_dessert = -1
#
#     for i in range(N):
#         for j in range(N):
#             visited = set()
#             visited.add(cafe[i][j])
#             max_dessert = max(max_dessert, dessert_ju_se_yo(i,j, i, j, visited, N, cafe))
#
#
#
#     print(f"#{tc} {max_dessert}")


def explore(x, y, start_x, start_y, direction, lst):
    if direction == 4:
        return

    nx = x + dx[direction]
    ny = y + dy[direction]
    if (nx, ny) == (start_x, start_y) and len(lst) >= 4:  # 사각형이 만들어 지면
        route.append(lst[:])
        return

    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] not in lst:
        lst.append(arr[nx][ny])
        explore(nx, ny, start_x, start_y, direction, lst)
        explore(nx, ny, start_x, start_y, direction + 1, lst)
        lst.pop()


T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dx = [1, 1, -1, -1] # 시계방향
    dy = [1, -1, -1, 1]
    route = []

    for i in range(n):
        for j in range(1,n-1):
            explore(i, j, i, j, 0, [arr[i][j]])

    if len(route) > 0:
        answer = max(len(i) for i in route)
        print(f'#{tc} {answer}')
    else:
        print(f'#{tc} -1')
