"""
삼성시 버스 5000개 정류장중
노선 N개 i번째 노선은 번호가 ai이상
bi이하인 몯느 정류장을 다니는 버스 노선.
P개의 버스 정류장에 대해 각 정류장에 몇개의 노선
"""
# 테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    # 노선수
    N = int(input())

    counts = [0] * 5001 # 5000번 정류장까지 진행
# ------------------------------------------------------------------------------
    # N개의 노선정보를 모두 읽어놓고 처리 or 읽을 때마다 처리

    for _ in range(N):
        # Ai -> Bi 버스 노선의 시점 Ai와 종점 Bi, Ai<=bi
        A, B = map(int, input().split())
        for i in range(A, B+1): # 1 <= Ai <= Bi <= 5000
            counts[i] += 1
    P = int(input()) # 노선수를 출력할 P개의 버스 정류장

# -------------------------------------------------------------------------------
    # 모두 읽어놓고 처리

    busstop = [int(input()) for _ in range(P)]

    print(f'#{tc}', end = ' ')

    for j in busstop: # 출력할 정류장 번호
        print(counts[j], end = ' ')
    print()