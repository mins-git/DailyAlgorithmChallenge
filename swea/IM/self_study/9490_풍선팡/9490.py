import sys
sys.stdin = open('input.txt')


"""
종이 꽃가루 풍선 M개씩 N개의 줄에 붙어있고,
풍선 안의 든 종이 꽃가루 개수만큼 상하좌우 추가로 터짐
최대로 터질 수 있는 꽃가루 개수 구해봐.
"""



T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split()) # N 줄에 걸쳐 M개씩 풍선이등 종이 꽃가루 주어짐
    arr = [list(map(int,  input().split())) for _ in range(N)] #꽃가루 개수
    max_flower_count = 0

    for r in range(N): # row만큼 순회
        for c in range(M): # col 만큼 순회
            flower_sum = arr[r][c]
            for dr, dc in [[0,1], [1,0], [0, -1], [-1, 0]] :
                nr, nc = r, c
                for p in range(arr[r][c]): # 방향만큼 다 더하면되잖아?
                    nr += dr
                    nc += dc
                    if 0 <= nr < N and 0 <= nc < M: # 범위를 벗어나지 않으면,
                        flower_sum += arr[nr][nc]
                    else: break

            if flower_sum > max_flower_count:
                max_flower_count = flower_sum

    print(f'#{tc} {max_flower_count}')