"""
꽃가루 개수만큼 상하좌우 풍선이 추가로 터지는 게임임!
한개의 풍선을 선택했을때, 날리는 꽃가루의 합중 최대값은? 출력
"""
# 아래 코드 수정 필요함
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     flower_matrix = [list(map(int,input().split())) for _ in range(N)]
#
#     max_v = 0 #꽃가루의 최대 합계
#     for i in range(N): # 터트려볼 풍선의 위치
#         for j in range(M):
#             cnt = flower_matrix[i][j] # 터트린 풍선에서 나오는 꽃가루의 개수
#             # 주변 풍선의 꽃가루 수
#             for k in range(4): #확인할 방향
#                 for l in range(1, flower_matrix[i][j]+1): #주변 방향으로 추가로 터지는 풍선과의 거리
#                     ni = i + di[k] * l
#                     nj = j + dj[k] * l
#                     if 0 <= ni < N and 0 <= nj < M :
#                         cnt += flower_matrix[ni][nj] # 주변 풍선에서 나오는 꽃가루 추가
#             if max_v < cnt: # for k에서 모든 꽃가루가 더해졌으니 비교
#                 max_v = cnt
#     print(f'#{tc} {max_v}')