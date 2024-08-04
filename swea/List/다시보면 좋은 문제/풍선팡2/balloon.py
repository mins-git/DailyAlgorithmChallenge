import sys

sys.stdin = open('input.txt')




# 종이 꽃가루가 N*M 크기의 격자판에 붙어있는데 풍선 터트리면
# 상하좌우의 풍선이 추가로 터지며 5개의 꽃가루 날리게됨
#
#
# N*M 풍선이 들어있는 종이 꽃가루 개수가 A/ 한개의 풍선을 선택해
# 터트리면 날릴 수 있는 꼬ㅓㅊ가루 수중 최대값
#
# 델타도 활용해야될것 같고, 상하좌우 델타검색 필요해보임.

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)] #[[2, 1, 1, 2, 2], [2, 2, 1, 2, 2], [2, 2, 1, 1, 2]]
    pollen = 0
    # 델타를 활용하여 상하좌우 순회하며 안에 몇개의 꽃가루가 있는지 확인하면 됨.

    dr = [0, 1, 0, -1]
    dc = [1, 0 ,-1, 0]


    for r in range(N):
        for c in range(M):
            count = arr[r][c] # 현재 카운트가 뭔지 확인하기
            for k in range(4):
                nr = r + dr[k]  # 현재 행에서 순회할 방향
                nc = c + dc[k]  # 현재 열에서 순회할 방향
                if 0 <= nr < N and 0 <= nc < M: # 각 엣지를 넘어서지 않게 정리
                    count += arr[nr][nc] # count에 각 꽃가루를 넣어주고 더하기
            if pollen < count:
                pollen = count

    print(f'#{tc} {pollen}')