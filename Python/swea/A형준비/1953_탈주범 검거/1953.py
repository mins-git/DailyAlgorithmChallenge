import sys

sys.stdin = open('input.txt', 'r')

"""
교도소로 이송 중이던 흉악범이 탈출하는 사건

탈주범 시간당 1의 거리 움직임.
7가지 구조물로 움직임
탈주범 있을 수 있는 지점 포함하여 15개 이다
"""

tunnel_type = {1: [(-1, 0), (1, 0), (0, -1), (0, 1)],  # 상 하 좌 우
               2: [(-1, 0), (1, 0)],  # 상 하
               3: [(0, -1), (0, 1)],  # 좌 우
               4: [(-1, 0), (0, 1)],  # 상 우
               5: [(1, 0), (0, 1)],  # 하 우
               6: [(1, 0), (0, -1)],  # 하 좌
               7: [(-1, 0), (0, -1)]  # 상 좌
               }

# 터널 간 연결 관계 확인.
def can_move(from_dir, to_tunnel):
    if from_dir == (-1,0): # 상에서 하로 가는 경우
        return to_tunnel in [1, 2, 5, 6] # 하향으로 연결될 수 있는 터널
    elif from_dir == (1, 0):  # 하에서 상으로 가려는 경우
        return to_tunnel in [1, 2, 4, 7]  # 상향으로 연결될 수 있는 터널
    elif from_dir == (0, -1):  # 좌에서 우로 가려는 경우
        return to_tunnel in [1, 3, 4, 5]  # 우향으로 연결될 수 있는 터널
    elif from_dir == (0, 1):  # 우에서 좌로 가려는 경우
        return to_tunnel in [1, 3, 6, 7]  # 좌향으로 연결될 수 있는 터널
    return False


def delta(tunnel, place, arr_r, arr_c, hour):
    # tunnel type에 키에 따른 방향만 delta 진행
    global cnt
    visited = [[False] * arr_c for _ in range(arr_r)]
    time = 0

    while time < hour:
        new_place = [] # 새로 이동할 위치 저장 리스트
        for r, c in place:

            if visited[r][c]:
                continue
            visited[r][c] = True
            cnt += 1

            delta_arr = tunnel_type.get(tunnel[r][c])  # key 3임 > #[(0, -1), (0, 1)] 뽑은 값의 델타 체크.

            for x, y in delta_arr:  # 2만큼 회전
                nr, nc = r + x, c + y  # 델타 될 위치 업데이트

                if 0 <= nr < arr_r and 0 <= nc < arr_c and not visited[nr][nc] and tunnel[nr][nc] != 0:  # 해당 tunnel의 값이 0이 아니고,
                    if can_move((x,y), tunnel[nr][nc]):
                        new_place.append([nr, nc])  # place에 해당 nr, nc 추가하기.

        place = new_place
        time += 1
        if time == hour:
            return cnt
    return cnt


T = int(input())

for tc in range(1, T + 1):
    # 세로의 크기 n, 가로의크기 m, 맨홀뚜껑 위치 세로 r 가로 c / 탈출 후 소요된 시간 L
    arr_r, arr_c, hole_r, hole_c, hour = map(int, input().split())

    tunnel = [list(map(int, input().split())) for _ in range(arr_r)]  # [[0, 0, 5, 3, 6, 0], [0, 0, 2, 0, 2, 0], [3, 3, 1, 3, 7, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

    place = [[hole_r, hole_c]]
    cnt = 0

    print(f'#{tc} {delta(tunnel, place, arr_r, arr_c, hour)}')